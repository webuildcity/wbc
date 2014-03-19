# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core import serializers
from projects.models import Ort, Veroeffentlichung, Verfahrensschritt, Verfahren, Behoerde, Bezirk
import datetime

def home(request):
    return render(request,'bbs/map.html')

def begriffe(request):
    verfahren = Verfahren.objects.all()
    return render(request,'bbs/begriffe.html',{'verfahren': verfahren})        
