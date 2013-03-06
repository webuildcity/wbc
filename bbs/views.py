from django.shortcuts import render
from django.core import serializers

from projects.models import Project,BBP

def home(request):
    p = Project.objects.all()
    b = BBP.objects.all()
    projectsJson = serializers.serialize("json", p)
    bbpJson = serializers.serialize("json", b) 
    return render(request,'bbs/map.html',{
            'baseUrl': request.path,
            'projectsJson': projectsJson,
            'bbpJson': bbpJson
            })
