# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import Http404, render
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt

import json,time,datetime

from projects.models import Ort, Veroeffentlichung, Verfahrensschritt, Verfahren, Behoerde, Bezirk

def orte(request):
    bezirk = request.GET.get('bezirk', None)
    vor = request.GET.get('vor', None)
    nach = request.GET.get('nach', None)

    orte = Ort.objects
    if vor:
        vor = tuple([int(i) for i in vor.split('-')])
        orte = orte.filter(veroeffentlichungen__ende__lte=datetime.date(*vor))
    if nach: 
        nach = tuple([int(i) for i in nach.split('-')])
        orte = orte.filter(veroeffentlichungen__ende__gte=datetime.date(*nach))
    if bezirk:
        orte = orte.filter(bezirke__name=bezirk)
    orte = orte.all()

    response = [ort_response(o) for o in orte]
    return HttpResponse(json.dumps(response,cls=DjangoJSONEncoder),content_type="application/json")

def ort(request, pk):
    try:
        ort = Ort.objects.get(pk=int(pk))
    except Ort.DoesNotExist:
        raise Http404

    return HttpResponse(json.dumps(ort_response(ort),cls=DjangoJSONEncoder),content_type="application/json")

def ort_response(ort):
    response = {
        'type': "Feature",
        'geometry': {
            'type': 'Point',
            'coordinates': [ort.lon,ort.lat]
        },
        'properties': {
            'pk': ort.pk,
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

def veroeffentlichungen(request):
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

    response = [veroeffentlichung_response(veroeffentlichung) for veroeffentlichung in veroeffentlichungen]
    return HttpResponse(json.dumps(response,cls=DjangoJSONEncoder),content_type="application/json")

def veroeffentlichung(request, pk):
    try:
        veroeffentlichung = Veroeffentlichung.objects.get(pk=int(pk))
    except Veroeffentlichung.DoesNotExist:
        raise Http404

    return HttpResponse(json.dumps(veroeffentlichung_response(veroeffentlichung),cls=DjangoJSONEncoder),content_type="application/json")

def veroeffentlichung_response(veroeffentlichung):
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

def verfahrensschritte(request):
    verfahrensschritte = Verfahrensschritt.objects.all()

    response = [verfahrensschritt_response(verfahrensschritt) for verfahrensschritt in verfahrensschritte]
    return HttpResponse(json.dumps(response,cls=DjangoJSONEncoder),content_type="application/json")

def verfahrensschritt(request, pk):
    try:
        verfahrensschritt = Verfahrensschritt.objects.get(pk=int(pk))
    except Verfahren.DoesNotExist:
        raise Http404

    return HttpResponse(json.dumps(verfahrensschritt_response(verfahrensschritt),cls=DjangoJSONEncoder),content_type="application/json")

def verfahrensschritt_response(verfahrensschritt):
    return {
        'pk': verfahrensschritt.pk,
        'name': verfahrensschritt.name,
        'beschreibung': verfahrensschritt.beschreibung,
        'icon': '/static/' + verfahrensschritt.icon,
        'hoverIcon': '/static/' + verfahrensschritt.hoverIcon
    }
