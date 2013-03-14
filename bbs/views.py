from django.shortcuts import render
from django.core import serializers
from projects.models import Project,BBP,Bezirk,Typ
import datetime

def home(request):
    p = Project.objects.all()
    b = BBP.objects.filter(end__gte = datetime.date.today())
    bezirke = Bezirk.objects.all()
    typ = Typ.objects.all()   
    projectsJson = serializers.serialize("json", p)
    bbpJson = serializers.serialize("json", b) 
    bezirkeJson = serializers.serialize("json", bezirke) 
    typJson = serializers.serialize("json", typ)
    return render(request,'bbs/map.html',{
            'baseUrl': request.path,
            'projectsJson': projectsJson,
            'bbpJson': bbpJson,
            'bezirkeJson': bezirkeJson,
            'typJson' : typJson
            })
