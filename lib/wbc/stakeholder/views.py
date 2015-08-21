# -*- coding: utf-8 -*-
from rest_framework import viewsets
from django.shortcuts import render

from models import *
from serializers import *

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
        # 'projects'       : Project.objects.filter(tags__name__in=[slug]).distinct(),
        # 'events'         : Event.objects.filter(tags__name__in=[slug]).distinct(),   
        # 'stakeholders'   : Stakeholder.objects.filter(tags__name__in=[slug]).distinct(),   
    })