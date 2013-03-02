from django.shortcuts import render

from projects.models import Project
from projects.models import BBP

def index(request):
    p = Project.objects.all()
    return render(request,'projects/index.html', {'projects': p})
    
def show(request, id):
    bbp = BBP.objects.get(pk=int(id))
    return render(request, 'projects/project.html', {'project':bbp})
