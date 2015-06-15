# -*- coding: utf-8 -*-
import datetime
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.utils.timezone import now
from django.views.generic.edit import CreateView
from django.template.loader import get_template
from django.template import Context

from rest_framework import viewsets
from rest_framework.response import Response

from wbc.core.views import ProtectedCreateView, ProtectedUpdateView, ProtectedDeleteView
from wbc.core.lib import send_mail
from wbc.region.models import District
from wbc.comments.models import Comment
from wbc.comments.forms import CommentForm

from participation.models import *

from models import *
from serializers import *
from forms import *


class PlaceViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(request, queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(request, instance)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Place.objects.all()
        active = self.request.query_params.get('active', None)

        if active is not None:
            queryset = queryset.filter(active=active)
        return queryset

    def get_serializer(self, request, queryset, **kwargs):
        geometry = self.request.query_params.get('geometry', None)

        if geometry == 'point':
            return PlacePointSerializer(queryset, **kwargs)
        elif geometry == 'polygon':
            return PlacePolygonSerializer(queryset, **kwargs)
        else:
            return PlaceSerializer(queryset, **kwargs)


class ListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ListSerializer

    paginate_by = 25
    paginate_by_param = 'page_size'

    def get_queryset(self):
        queryset = Place.objects.all()

        search = self.request.query_params.get('search', None)
        if search is not None:
            queryset = queryset.filter(Q(identifier__icontains=search) | Q(address__icontains=search) | Q(entities__name__icontains=search))

        return queryset


class MapViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MapSerializer
    delta = now() - datetime.timedelta(days=100)
    queryset = Place.objects.all().filter(publications__end__gte=delta)


class PublicationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()


class ProcessStepViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProcessStepSerializer
    queryset = ProcessStep.objects.all()


class ProcessTypeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProcessTypeSerializer
    queryset = ProcessType.objects.all()


class PlaceCreate(ProtectedCreateView):
    model = Place
    fields = '__all__'


class PlaceUpdate(ProtectedUpdateView):
    model = Place
    fields = '__all__'


class PlaceDelete(ProtectedDeleteView):
    model = Place
    success_url = reverse_lazy('places')


class PublicationCreate(ProtectedCreateView):
    model = Publication
    fields = '__all__'

    def get_initial(self):
        try:
            self.initial['place'] = Place.objects.get(pk=self.request.GET.get('place_id', None))
        except Place.DoesNotExist:
            self.initial['place'] = {}
        return self.initial


class PublicationUpdate(ProtectedUpdateView):
    model = Publication
    fields = '__all__'


class PublicationDelete(ProtectedDeleteView):
    model = Publication

    def get_success_url(self):
        return self.object.place.get_absolute_url()


def process(request):
    process_types = ProcessType.objects.all()
    return render(request, 'process/process.html', {'process_types': process_types})

def places(request):
    return render(request, 'process/list.html', {'new_place_link': reverse('place_create')})

def place(request, pk):
    p = get_object_or_404(Place, id=int(pk))

    if request.method == 'POST':
        if len(request.POST["author_email1"]) == 0:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.enabled = True
                comment.place = p
                comment.save()

    return render(request, 'process/place.html', {
        'place': p,
        'comments': Comment.objects.filter(place_id=int(pk), enabled=True),
        'process_link': reverse('wbc.process.views.process'),
        'new_publication_link': reverse('publication_create'),
        'new_participation_link': reverse('participation_create'),
    })

class ParticipationCreate(CreateView):
    fields = '__all__'

    def dispatch(self, *args, **kwarg):
        publication_id = self.request.GET.get('publication_id', None)

        self.publication = Publication.objects.get(pk=publication_id)
        querystring = self.publication.process_step.participation
        participation = get_object_or_404(ContentType, app_label='participation', model=querystring)
        self.participation_class = participation.model_class()
        return super(ParticipationCreate, self).dispatch(*args, **kwarg)

    def get_template_names(self):
        return ['process/publication.html']

    def get_queryset(self):
        return self.participation_class.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ParticipationCreate, self).get_context_data(**kwargs)
        context['publication'] = self.publication
        return context

    def form_valid(self, form):
        form.instance.publication = self.publication

        if self.publication.email:

            send_mail(self.publication.email, 'process/mail/participation.html', {
                'form': form,
                'publication': self.publication
            })

        return super(ParticipationCreate, self).form_valid(form)


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
        title = item.process_step.process_type.name + ': ' +  item.process_step.name

        l = []
        if item.place.identifier != '':
            l.append(item.place.identifier)

        try:
            l.append(item.place.entities.all()[0].name)
        except IndexError:
            pass

        if l != []: title += ' (' + ', '.join(l) + ')'

        return title

    def item_description(self, item):
        return item.description

    def item_guid(self, item):
        return str(item.pk)

    def item_pubdate(self, item):
        return item.created

    def item_link(self, item):
        return settings.SITE_URL + reverse('wbc.process.views.place', args=[item.place.pk])
