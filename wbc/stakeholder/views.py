# -*- coding: utf-8 -*-
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse


from wbc.core.views import ProtectedCreateView, ProtectedUpdateView, ProtectedDeleteView
from wbc.projects.models import Project
from models import *
from serializers import *
from forms import *

class StakeholderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StakeholderSerializer
    queryset = Stakeholder.objects.all()

class StakeholderRoleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StakeholderRoleSerializer
    queryset = StakeholderRole.objects.all()

class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

def stakeholderview(request, slug):
    s = Stakeholder.objects.get(slug__iexact=slug)
    notifications = None
    ownprojects = None
    try:
        if request.user == s.profile.user:
            if s.profile.subscriber:
                notifications = s.profile.subscriber.projects.all()
        ownprojects = Project.objects.filter(owner=s.profile.user)
    except:
        print 'no profile'

    return render(request,'stakeholder/stakeholder.html',{
        'stakeholder'       : s,
        'own_projects'      : ownprojects,
        'projects'          : Project.objects.filter(stakeholders=s.id).distinct(),
        'tags'              : s.tags.all(),
        'notifications'     : notifications
        # 'events'         : Event.objects.filter(tags__name__in=[slug]).distinct(),   
        # 'stakeholders'   : Stakeholder.objects.filter(tags__name__in=[slug]).distinct(),   
    })


class StakeholderCreate(ProtectedCreateView):
    model = Stakeholder
    form_class = StakeholderForm

    def get_initial(self):
        initial_data = super(StakeholderCreate, self).get_initial()
        try:
            initial_data['projects']= [Project.objects.get(pk=self.request.GET.get('project_id'))]
        except Project.DoesNotExist:
            initial_data['projects'] = []
        return initial_data

    def form_valid(self, form):
        self.object = form.save()
        url = self.object.project_set.all()[0].get_absolute_url()
        return JsonResponse({'redirect': url})

    def form_invalid(self, form):
        response = super(StakeholderCreate, self).form_invalid(form)
        return response


class StakeholderUpdate(ProtectedUpdateView):
    model = Stakeholder
    form_class = StakeholderForm

    def get_initial(self):
        initial_data = super(StakeholderUpdate, self).get_initial()
        try:
            initial_data['projects']= self.object.project_set.all()
        except Project.DoesNotExist:
            initial_data['projects'] = []
        return initial_data

    def form_valid(self, form):
        self.object = form.save()
        url = self.object.project_set.all()[0].get_absolute_url()
        return JsonResponse({'redirect': url})

    def form_invalid(self, form):
        response = super(StakeholderUpdate, self).form_invalid(form)
        return response

class StakeholderDelete(ProtectedDeleteView):
    model = Stakeholder

    def get_success_url(self):
        return self.object.project_set.all()[0].get_absolute_url()


def photo_upload(request, pk):
    """
    View for uploading photos via AJAX.
    """
    stakeholder = get_object_or_404(Stakeholder, id= int(pk))
    if request.user.has_perm('stakeholder.change_stakeholder', stakeholder):
        uploaded_file = request.FILES['file']
        # Photo.objects.create(album=album, file=uploaded_file)
        stakeholder.picture = uploaded_file
        stakeholder.save()
        response_dict = {
            'message': 'File uploaded successfully!',
        }

        return HttpResponse(response_dict, content_type='application/json')
    else:
        response_dict = {'message': 'No Permission!',}
        return HttpResponse(response_dict, content_type='application/json')
