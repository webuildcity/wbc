from django.shortcuts import render
from django.core import serializers

from projects.models import Project

def home(request):
    p = Project.objects.all()
    json = serializers.serialize("json", p)
    return render(request,'bbs/map.html', {'projectsJson': json})
