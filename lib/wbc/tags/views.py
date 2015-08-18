# -*- coding: utf-8 -*-
from rest_framework import viewsets

from models import *
from wbc.projects.models  import Project
from serializers import *
from django.shortcuts import render,get_object_or_404


def tagview(request, slug):
    t = Tag.objects.get(slug__iexact=slug)

    return render(request,'tags/tag.html',{
        'tag'      : t,
        'projects' : Project.objects.filter(tags = int(t.pk))
        # 'comments': Comment.objects.filter(project = int(p.pk), enabled = True),
        # 'events'  : Event.objects.filter(projects = int(p.pk)).order_by('-begin'),   
        # 'gallery' : gallery,
        # 'nextDate': Date.objects.filter(projects = int(p.pk), begin__gte=today).order_by('begin').first(),
        # 'lastNews': Media.objects.filter(projects = int(p.pk)).order_by('begin').first(),
        # 'tags'    : Tag.objects.filter(tags_project = int(p.pk))
    })