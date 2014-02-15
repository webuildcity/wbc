# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import Http404, render
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
import json

import lib.views

from projects.models import Ort, Veroeffentlichung, Verfahrensschritt, Verfahren, Behoerde, Bezirk

def createGeoJson(ort):
    response = {
        'type': "Feature",
        'geometry': {
            'type': 'Point',
            'coordinates': [ort.lon,ort.lat]
        },
        'properties': {
            'bezeichner': ort.bezeichner,
            'adresse': ort.adresse,
            'beschreibung': ort.beschreibung,
            'bezirke': [],
            'veroeffentlichungen': []
        }
    }
    for bezirk in ort.bezirke.all():
        response['properties']['bezirke'].append(bezirk.name)
    for veroeffentlichung in ort.veroeffentlichungen.all():
        response['properties']['veroeffentlichungen'].append({
            'beschreibung': veroeffentlichung.beschreibung,
            'verfahrensschritt': veroeffentlichung.verfahrensschritt.name,
            'beginn': veroeffentlichung.beginn,
            'ende': veroeffentlichung.ende,
            'auslegungsstelle': veroeffentlichung.auslegungsstelle,
            'behoerde': veroeffentlichung.behoerde.name,
            'link': veroeffentlichung.link
        })
    return response

class OrteView(lib.views.View):
    http_method_names = ['get']

    def get(self, request):
        bezirk = request.GET.get('bezirk', None)

        if bezirk:
            orte = Ort.objects.filter(bezirke__name=bezirk)
        else: 
            orte = Ort.objects.all()

        if self.accept == 'json':
            response = {'type': 'FeatureCollection','features': []}
            for ort in orte:
                response['features'].append(createGeoJson(ort))
            return self.renderJson(request,response)
        else:
            response = {'orte': orte}
            return render(request,'projects/orte.html', response)

class OrtView(lib.views.View):
    http_method_names = ['get']

    def get(self, request, pk):
        try:
            ort = Ort.objects.get(pk=int(pk))
        except Ort.DoesNotExist:
            raise Http404

        if self.accept == 'json':
            response = createGeoJson(ort)
            return self.renderJson(request, response)
        else:
            response = {'ort': ort}
            return render(request, 'projects/ort.html', response)
