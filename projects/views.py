# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import Http404, render
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt

import json,time,datetime

import lib.views

from projects.models import Ort, Veroeffentlichung, Verfahrensschritt, Verfahren, Behoerde, Bezirk

class OrtView(lib.views.View):
    http_method_names = ['get']

    def constructOrtJsonDict(self, ort):
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
                'verfahrensschritt': {
                    'pk': veroeffentlichung.verfahrensschritt.pk,
                    'name': veroeffentlichung.verfahrensschritt.name,
                    'verfahren': veroeffentlichung.verfahrensschritt.verfahren.name
                },
                'beginn': veroeffentlichung.beginn,
                'ende': veroeffentlichung.ende,
                'auslegungsstelle': veroeffentlichung.auslegungsstelle,
                'behoerde': veroeffentlichung.behoerde.name,
                'link': veroeffentlichung.link
            })

        return response

    def constructJsonDict(self, context):
        if 'orte' in context:
            response = {'type': 'FeatureCollection','features': []}
            for ort in context['orte']:
                response['features'].append(self.constructOrtJsonDict(ort))
        else:
            response = self.constructOrtJsonDict(context['ort'])

        return response

    def get_objects(self, request):
        bezirk = request.GET.get('bezirk', None)
        beginn = request.GET.get('beginn', None)
        ende = request.GET.get('ende', None)

        orte = Ort.objects
        if beginn:
            beginn = tuple([int(i) for i in beginn.split('-')])
            orte = orte.filter(veroeffentlichungen__beginn__lte=datetime.date(*beginn))
        if ende: 
            ende = tuple([int(i) for i in ende.split('-')])
            orte = orte.filter(veroeffentlichungen__ende__gte=datetime.date(*ende))
        if bezirk:
            orte = orte.filter(bezirke__name=bezirk)
        orte = orte.all()

        context = {'orte': orte}
        return self.render(request,'projects/orte.html', context)

    def get_object(self, request, pk):
        try:
            ort = Ort.objects.get(pk=int(pk))
        except Ort.DoesNotExist:
            raise Http404

        context = {'ort': ort}
        return self.render(request, 'projects/ort.html', context)

class VeroeffentlichungView(lib.views.View):
    http_method_names = ['get']

    def constructVeroeffentlichungJsonDict(self, veroeffentlichung):
        return {
            'beschreibung': veroeffentlichung.beschreibung,
            'verfahrensschritt': veroeffentlichung.verfahrensschritt.name,
            'beginn': veroeffentlichung.beginn,
            'ende': veroeffentlichung.ende,
            'auslegungsstelle': veroeffentlichung.auslegungsstelle,
            'behoerde': veroeffentlichung.behoerde.name,
            'link': veroeffentlichung.link,
            'ort': veroeffentlichung.ort.adresse,
            'bezirk': ', '.join([b.name for b in veroeffentlichung.ort.bezirke.all()])
        }

    def constructJsonDict(self, context):
        if 'veroeffentlichungen' in context:
            response = []
            for veroeffentlichung in context['veroeffentlichungen']:
                response.append(self.constructVeroeffentlichungJsonDict(veroeffentlichung))
        else:
            response = self.constructVeroeffentlichungJsonDict(context['veroeffentlichung'])

        return response

    def get_objects(self, request):
        beginn = request.GET.get('beginn', None)
        ende = request.GET.get('ende', None)

        veroeffentlichungen = Veroeffentlichung.objects
        if beginn:
            beginn = tuple([int(i) for i in beginn.split('-')])
            veroeffentlichungen = veroeffentlichungen.filter(beginn__lte=datetime.date(*beginn))
        if ende: 
            ende = tuple([int(i) for i in ende.split('-')])
            veroeffentlichungen = veroeffentlichungen.filter(ende__gte=datetime.date(*ende))
        veroeffentlichungen = veroeffentlichungen.all()

        context = {'veroeffentlichungen': veroeffentlichungen}
        return self.render(request,'projects/veroeffentlichungen.html', context)

    def get_object(self, request, pk):
        try:
            veroeffentlichung = Veroeffentlichung.objects.get(pk=int(pk))
        except Veroeffentlichung.DoesNotExist:
            raise Http404

        context = {'veroeffentlichung': veroeffentlichung}
        return self.render(request, 'projects/veroeffentlichung.html', context)

class VerfahrenView(lib.views.View):
    http_method_names = ['get']

    def constructVerfahrenJsonDict(self, verfahren):
        return {
            'pk': verfahren.pk,
            'name': verfahren.name,
            'beschreibung': verfahren.beschreibung
        }

    def constructJsonDict(self, context):
        if 'verfahrens' in context:
            response = []
            for verfahren in context['verfahrens']:
                response.append(self.constructVerfahrenJsonDict(verfahren))
        else:
            response = self.constructVerfahrenJsonDict(context['verfahren'])

        return response

    def get_objects(self, request):
        verfahrens = Verfahren.objects.all()
        
        context = {'verfahrens': verfahrens}
        return self.render(request,'projects/verfahrens.html', context)

    def get_object(self, request, pk):
        try:
            verfahren = Verfahren.objects.get(pk=int(pk))
        except Verfahren.DoesNotExist:
            raise Http404

        context = {'verfahren': verfahren}
        return self.render(request, 'projects/verfahren.html', context)

class VerfahrensschrittView(lib.views.View):
    http_method_names = ['get']

    def constructVerfahrensschrittJsonDict(self, verfahrensschritt):
        return {
            'pk': verfahrensschritt.pk,
            'name': verfahrensschritt.name,
            'beschreibung': verfahrensschritt.beschreibung,
             'icon': verfahrensschritt.icon,
             'hoverIcon': verfahrensschritt.hoverIcon
        }

    def constructJsonDict(self, context):
        if 'verfahrensschritte' in context:
            response = []
            for verfahrensschritt in context['verfahrensschritte']:
                response.append(self.constructVerfahrensschrittJsonDict(verfahrensschritt))
        else:
            response = self.constructVerfahrensschrittJsonDict(context['verfahrensschritt'])

        return response

    def get_objects(self, request):
        verfahrensschritte = Verfahrensschritt.objects.all()
        context = {'verfahrensschritte': verfahrensschritte}
        return self.render(request,'projects/verfahrensschritte.html', context)

    def get_object(self, request, pk):
        try:
            verfahrensschritt = Verfahrensschritt.objects.get(pk=int(pk))
        except Verfahren.DoesNotExist:
            raise Http404

        context = {'verfahrensschritt': verfahrensschritt}
        return self.render(request, 'projects/verfahrensschritt.html', context)
    

