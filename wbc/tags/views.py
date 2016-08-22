# -*- coding: utf-8 -*-
from rest_framework import viewsets

from models import *
from wbc.projects.models  import Project
from wbc.events.models import Event
from wbc.stakeholder.models import Stakeholder
from serializers import *
from django.shortcuts import render,get_object_or_404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def tagview(request, slug):
    t = WbcTag.objects.get(slug__iexact=slug)
    projects = Project.objects.filter(tags__in=[t]).distinct()
    stakeholders = Stakeholder.objects.filter(tags__in=[t]).distinct()
    events = Event.objects.filter(tags__in=[t]).distinct()
    projects_paginator_full = Paginator(projects, 3)
    if request.method == 'GET':
        page = request.GET.get('page')
        try:
            projects_paginator = projects_paginator_full.page(page)
        except PageNotAnInteger:
            projects_paginator = projects_paginator_full.page(1)
        except EmptyPage:
            projects_paginator = projects_paginator_full.page(projects_paginator_full.num_pages)

    

    return render(request,'tags/tag.html',{
        'tag'             : t,
        'projects'        : projects_paginator,
        'projects_len'    : len(projects),
        'events'          : events,   
        'stakeholders'    : stakeholders,   
        'stakeholders_len': len(stakeholders),   
    })