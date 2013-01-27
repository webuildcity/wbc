from django.shortcuts import render

from projects.models import Project

def index(request):
    p = Project.objects.all()
    return render(request,'projects/index.html', {'projects': p})
