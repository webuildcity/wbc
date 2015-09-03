# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.utils.feedgenerator import Rss201rev2Feed
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404

from rest_framework import viewsets

from models import *
from serializers import *

from wbc.core.views import ProtectedCreateView, ProtectedUpdateView, ProtectedDeleteView
from wbc.region.models import District
from wbc.events.models import Publication
from wbc.projects.models import Project


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class DateViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DateSerializer
    queryset = Date.objects.all()

class MediaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()

class PublicationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()

class PublicationFeedMimeType(Rss201rev2Feed):
    mime_type = 'application/xml'

class PublicationCreate(ProtectedCreateView):
    model = Publication
    fields = '__all__'

    def get_initial(self):
        try:
            self.initial['project'] = Project.objects.get(
                pk=self.request.GET.get('project_id', None))
        except Project.DoesNotExist:
            self.initial['project'] = {}
        return self.initial


class PublicationUpdate(ProtectedUpdateView):
    model = Publication
    fields = '__all__'


class PublicationDelete(ProtectedDeleteView):
    model = Publication

    def get_success_url(self):
        return self.object.project.get_absolute_url()


class PublicationFeed(Feed):
    title = settings.FEED_TITLE
    description = settings.FEED_DESCRIPTION
    link = settings.SITE_URL
    feed_url = '/feeds/'
    feed_type = PublicationFeedMimeType

    def get_object(self, request):
        if 'bezirk' in request.GET:
            district = request.GET['bezirk']
            try:
                District.objects.get(name=district)
            except District.DoesNotExist:
                raise Http404
            return Publication.objects.filter(project__entities__name=district)
        return Publication.objects

    def items(self, objs):
        return objs.order_by('-created')[:10]

    def item_title(self, item):
        title = item.process_step.process_type.name + \
            ': ' + item.process_step.name

        l = []
        if item.project.name != '':
            l.append(item.project.name)
        try:
            l.append(item.project.entities.all()[0].name)
        except IndexError:
            pass

        if l != []:
            title += ' (' + ', '.join(l) + ')'

        return title

    def item_description(self, item):
        return item.description

    def item_guid(self, item):
        return str(item.pk)

    def item_pubdate(self, item):
        return item.created

    def item_link(self, item):
        return settings.SITE_URL + reverse('wbc.projects.views.project', args=[item.project.pk])
