# -*- coding: utf-8 -*-
from rest_framework import viewsets
from django.shortcuts import render
from django.http import JsonResponse

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

    return render(request,'stakeholder/stakeholder.html',{
        'stakeholder'       : s,
        'projects'          : Project.objects.filter(stakeholders=s.id).distinct(),
        'tags'              : s.tags.all()
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
