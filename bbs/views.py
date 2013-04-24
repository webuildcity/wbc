# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core import serializers
from projects.models import Project,BBP,Bezirk,Typ
import datetime

def home(request):
    p = Project.objects.all()
    b = BBP.objects.filter(end__gte = datetime.date.today(), typ__name = u'Öffentliche Auslegung')
    b_frueh = BBP.objects.filter(end__gte = datetime.date.today(), typ__name = u'Frühzeitige Öffentlichkeitsbeteiligung')
    b_erneut = BBP.objects.filter(end__gte = datetime.date.today(), typ__name = u'Erneute öffentliche Auslegung')
    bOld = BBP.objects.filter(end__lt = datetime.date.today())
    bezirke = Bezirk.objects.all()
    typ = Typ.objects.all() 
      
    projectsJson = serializers.serialize("json", p)
    
    bbpJson = serializers.serialize("json", b) 
    bbpFruehJson = serializers.serialize("json", b_frueh) 
    bbpErneutJson = serializers.serialize("json", b_erneut) 
    bbpOldJson = serializers.serialize("json", bOld) 
    
    bezirkeJson = serializers.serialize("json", bezirke) 
    typJson = serializers.serialize("json", typ)
    
    return render(request,'bbs/map.html',{
            'baseUrl': request.path,
            'projectsJson': projectsJson,
            'bbpJson': bbpJson,
            'bbpFruehJson': bbpFruehJson,
            'bbpErneutJson': bbpErneutJson,
            'bbpOldJson': bbpOldJson,
            'bezirkeJson': bezirkeJson,
            'typJson' : typJson,
            'typ' : typ
            })
