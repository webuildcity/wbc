# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core import serializers
from projekte.models import Projekt, Veroeffentlichung, Verfahrensschritt, Verfahren, Behoerde, Bezirk
import datetime,json

def home(request):
    verfahren = Verfahren.objects.all()

    verfahrensschritte = []
    for v in Verfahrensschritt.objects.all():
        verfahrensschritt = {
            'pk': v.pk,
            'name': v.name,
            'icon': v.icon
        }
        verfahrensschritte.append(verfahrensschritt);

    points = []
    for v in Veroeffentlichung.objects.filter(ende__gte = datetime.date.today()):
        point = {
            'pk': v.pk,
            'ende': unicode(v.ende),
            'behoerde': v.behoerde.name,
            'projekt': v.projekt.pk,
            'adresse': v.projekt.adresse,
            'lat': v.projekt.lat,
            'lon': v.projekt.lon,
            'vspk': v.verfahrensschritt.pk,
        }
        points.append(point);

    # bOld = BBP.objects.filter(end__lt = datetime.date.today())

    return render(request,'bbs/map.html',{'points': json.dumps(points),'verfahrensschritte': json.dumps(verfahrensschritte), 'verfahren': verfahren})

def info(request):
    verfahren = Verfahren.objects.all()
    return render(request,'bbs/info.html',{'verfahren': verfahren})        
