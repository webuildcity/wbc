# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core import serializers
from projekte.models import Projekt, Veroeffentlichung, Verfahrensschritt, Verfahren, Behoerde, Bezirk
import datetime

def home(request):
    verfahren = Verfahren.objects.all()
    verfahrensschritte = Verfahrensschritt.objects.all()
    veroeffentlichungen = Veroeffentlichung.objects.filter(ende__gte = datetime.date.today())
    veroeffentlichungenAlt = Veroeffentlichung.objects.filter(ende__lt = datetime.date.today())

    return render(request,'bbs/map.html',{
        'verfahrensschritte': verfahrensschritte,
        'verfahren': verfahren,
        'veroeffentlichungen': veroeffentlichungen,
        'veroeffentlichungenAlt': veroeffentlichungenAlt,
        'absolute': True
        })

def begriffe(request):
    verfahren = Verfahren.objects.all()
    return render(request,'bbs/begriffe.html',{'verfahren': verfahren})        
