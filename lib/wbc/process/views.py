# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets

from models import *
from serializers import *

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

# def ort(request,pk):
#     ort = get_object_or_404(Ort, id = int(pk))
#     if request.method == 'POST':
#         if len(request.POST["author_email1"]) == 0:
#             kommentar_neu = KommentarForm(request.POST)
#             if kommentar_neu.is_valid():
#                 kommentar = kommentar_neu.save(commit=False)
#                 kommentar.enabled = True;
#                 kommentar.ort = ort
#                 kommentar.save()

#     kommentare = Kommentar.objects.filter(ort_id = int(pk), enabled = True)
#     return render(request, 'core/ort.html', {'ort': ort, 'kommentare': kommentare})

# def feeds(request):
#     bezirke = Bezirk.objects.all()
#     return render(request,'core/feeds.html',{'bezirke': bezirke})

# @login_required
# def create_veroeffentlichung(request):
#     orte_id = request.GET.get('orte_id', None)

#     if orte_id == None:
#         form = FindOrt()
#         return render(request, 'core/create_veroeffentlichung_step1.html', {'form':form})

#     else:
#         ort = Ort.objects.get(pk=orte_id)

#         if request.method == 'POST':
#             form = CreateVeroeffentlichung(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return HttpResponseRedirect('/orte/' + str(ort.pk))
#             else:
#                 return render(request, 'core/create_veroeffentlichung_step2.html', {'form':form})
#         else:
#             form = CreateVeroeffentlichung(initial={'ort': ort})
#             return render(request,'core/create_veroeffentlichung_step2.html',{'form':form})

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
