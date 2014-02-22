# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import Http404, render
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt

import json,time,datetime

import lib.views

from projects.models import Ort, Veroeffentlichung, Verfahrensschritt, Verfahren, Behoerde, Bezirk

class AbstractOrteView(lib.views.View):
    http_method_names = ['get']

    def response(self, ort):
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

class OrteView(AbstractOrteView):
    def get(self, request):
        bezirk = request.GET.get('bezirk', None)

        if bezirk:
            orte = Ort.objects.filter(bezirke__name=bezirk)
        else: 
            orte = Ort.objects.all()

        if self.accept == 'json':
            response = {'type': 'FeatureCollection','features': []}
            for ort in orte:
                response['features'].append(self.response(ort))
            return self.renderJson(request,response)
        else:
            response = {'orte': orte}
            return render(request,'projects/orte.html', response)

class OrtView(AbstractOrteView):
    def get(self, request, pk):
        try:
            ort = Ort.objects.get(pk=int(pk))
        except Ort.DoesNotExist:
            raise Http404

        if self.accept == 'json':
            return self.renderJson(request, self.response(ort))
        else:
            response = {'ort': ort}
            return render(request, 'projects/ort.html', response)

class AbstractVeroeffentlichungView(lib.views.View):
    http_method_names = ['get']

    def response(self, veroeffentlichung):
        return {
            'beschreibung': veroeffentlichung.beschreibung,
            'verfahrensschritt': veroeffentlichung.verfahrensschritt.name,
            'beginn': veroeffentlichung.beginn,
            'ende': veroeffentlichung.ende,
            'auslegungsstelle': veroeffentlichung.auslegungsstelle,
            'behoerde': veroeffentlichung.behoerde.name,
            'link': veroeffentlichung.link,
            'ort': veroeffentlichung.ort.adresse
        }

class VeroeffentlichungenView(AbstractVeroeffentlichungView):
    def get(self, request):
        beginn = request.GET.get('beginn', None)
        ende = request.GET.get('ende', None)

        veroeffentlichungen = Veroeffentlichung.objects
        if beginn:
            beginn = tuple([int(i) for i in beginn.split('-')])
            print beginn
            veroeffentlichungen = veroeffentlichungen.filter(beginn__gte=datetime.date(*beginn))
        if ende: 
            ende = tuple([int(i) for i in ende.split('-')])
            veroeffentlichungen = veroeffentlichungen.filter(ende__lte=datetime.date(*ende))
        veroeffentlichungen = veroeffentlichungen.all()

        if self.accept == 'json':
            response = []
            for veroeffentlichung in veroeffentlichungen:
                response.append(self.response(veroeffentlichung))
            return self.renderJson(request,response)
        else:
            response = {'veroeffentlichungen': veroeffentlichungen}
            return render(request,'projects/veroeffentlichungen.html', response)

class VeroeffentlichungView(AbstractVeroeffentlichungView):
    def get(self, request, pk):
        try:
            veroeffentlichung = Veroeffentlichung.objects.get(pk=int(pk))
        except Veroeffentlichung.DoesNotExist:
            raise Http404

        if self.accept == 'json':
            return self.renderJson(request, self.response(veroeffentlichung))
        else:
            response = {'veroeffentlichung': veroeffentlichung}
            return render(request, 'projects/ort.html', response)

