from django.shortcuts import get_object_or_404

from bbs.lib import RestView
from projects.models import Project,BBP

class ProjectsView(RestView):

    def get_items(self, request):
        projects = Project.objects.all()
        response = {'projects': projects}
        return self.render(request,'projects/projects.html', response)

    def get_item(self, request, pk):
        project = Project.objects.get(pk=int(pk))
        response = {'project': project}
        return self.render(request,'projects/project.html', response)
 
class BBPView(RestView):

    def get_items(self, request):
        projects = BBP.objects.all()
        response = {'projects': projects}
        return self.render(request,'projects/projects.html', response)

    def get_item(self, request, pk):
        project = BBP.objects.get(pk=int(pk))
        response = {'project': project}
        return self.render(request,'projects/project.html', response)
