# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework import viewsets

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

# def feeds(request):
#     bezirke = Bezirk.objects.all()
#     return render(request,'core/feeds.html',{'bezirke': bezirke})

# class VeroeffentlichungenFeedMimeType(Rss201rev2Feed):
#     mime_type = 'application/xml'

# class VeroeffentlichungenFeed(Feed):
#     title = "Bürger baut Stadt (Veröffentlichungen)"
#     description = "Veröffentlichungen zu Bauvorhaben in Berlin"
#     link = settings.SITE_URL
#     feed_url = settings.SITE_URL + "/veroeffentlichungen/feed/"
#     feed_type = VeroeffentlichungenFeedMimeType

#     def get_object(self, request):
#         if 'bezirk' in request.GET:
#             bezirk = request.GET['bezirk']
#             try:
#                 Bezirk.objects.get(name=bezirk)
#             except Bezirk.DoesNotExist:
#                 raise Http404
#             return Veroeffentlichung.objects.filter(ort__bezirke__name=bezirk)
#         return Veroeffentlichung.objects

#     def items(self, objs):
#         return objs.order_by('-created')[:10]

#     def item_title(self, item):
#         return item.verfahrensschritt.verfahren.name + ': ' +  item.verfahrensschritt.name + ' (' + item.ort.bezeichner + ', ' + item.ort.bezirke.all()[0].name + ')'

#     def item_description(self, item):
#         return item.beschreibung

#     def item_guid(self, item):
#         return str(item.pk)

#     def item_pubdate(self, item):
#         return item.created

#     def item_link(self, item):
#         return settings.SITE_URL + '/orte/' + str(item.ort.pk)
