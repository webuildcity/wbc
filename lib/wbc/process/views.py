# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework import viewsets

from wbc.region.models import District
from wbc.comments.models import Comment
from wbc.comments.forms import CommentForm
from models import *
from serializers import *
from forms import *

class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

class PublicationViewSet(viewsets.ModelViewSet):
    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()

class ProcessStepViewSet(viewsets.ModelViewSet):
    serializer_class = ProcessStepSerializer
    queryset = ProcessStep.objects.all()

class ProcessTypeViewSet(viewsets.ModelViewSet):
    serializer_class = ProcessTypeSerializer
    queryset = ProcessType.objects.all()

def process(request):
    process_types = ProcessType.objects.all()
    return render(request,'process/process.html',{'process_types': process_types})

def place(request, pk):
    p = get_object_or_404(Place, id = int(pk))

    if request.method == 'POST':
        if len(request.POST["author_email1"]) == 0:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.enabled = True;
                comment.place = p
                comment.save()

    return render(request,'process/place.html',{
        'place': p,
        'comments': Comment.objects.filter(place_id = int(pk), enabled = True),
        'process_link': reverse('wbc.process.views.process'),
        'new_publication_link': reverse('wbc.process.views.create_publication')
    })

@login_required
def create_publication(request):
    place_id = request.GET.get('place_id', None)
    place_url = reverse('wbc.process.views.place',args=['1'])[:-2]

    if place_id == None:
        form = FindPlace()
        return render(request, 'process/create_publication_step_1.html', {
            'form': form,
            'new_publication_link': reverse('wbc.process.views.create_publication')
        })

    else:
        place = Place.objects.get(pk=place_id)

        if request.method == 'POST':
            form = CreatePublication(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(place_url + str(place.pk))
            else:
                return render(request, 'process/create_publication_step_2.html', {'form': form})
        else:
            form = CreatePublication(initial={'place': place})
            return render(request,'process/create_publication_step_2.html',{'form': form})

class PublicationFeedMimeType(Rss201rev2Feed):
    mime_type = 'application/xml'

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
            return Publication.objects.filter(place__entities__name=district)
        return Publication.objects

    def items(self, objs):
        return objs.order_by('-created')[:10]

    def item_title(self, item):
        return item.process_step.process_type.name + ': ' +  item.process_step.name + ' (' + item.place.identifier + ', ' + item.place.entities.all()[0].name + ')'

    def item_description(self, item):
        return item.description

    def item_guid(self, item):
        return str(item.pk)

    def item_pubdate(self, item):
        return item.created

    def item_link(self, item):
        return settings.SITE_URL + reverse('wbc.process.views.place', args=[item.place.pk])
