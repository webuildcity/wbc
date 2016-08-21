# -*- coding: utf-8 -*-
from rest_framework import viewsets

from models import *
from wbc.projects.models  import Project
from wbc.events.models import Event
from wbc.stakeholder.models import Stakeholder
from serializers import *
from django.shortcuts import render,get_object_or_404


def tagview(request, slug):
    t = WbcTag.objects.get(slug__iexact=slug)
    return render(request,'tags/tag.html',{
        'tag'             : t,
        'projects'        : Project.objects.filter(tags__in=[t]).distinct()[:3],
        'projects_len'    : len(Project.objects.filter(tags__in=[t]).distinct()),
        'events'          : Event.objects.filter(tags__in=[t]).distinct(),   
        'stakeholders'    : Stakeholder.objects.filter(tags__in=[t]).distinct()[:3],   
        'stakeholders_len': len(Stakeholder.objects.filter(tags__in=[t]).distinct()),   
    })