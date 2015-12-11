# -*- coding: utf-8 -*-
import datetime
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from django.http import HttpResponseRedirect, Http404
from django.db.models import Q
from django.utils.timezone import now

from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializers import *
from .forms import *


class ProcessStepViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProcessStepSerializer
    queryset = ProcessStep.objects.all()


class ProcessTypeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProcessTypeSerializer
    queryset = ProcessType.objects.all()

def process(request, pk=None):
    entries = ProcessType.encyclopedia_entry.objects.all()
    if pk:
        process_step = get_object_or_404(ProcessStep, pk=int(pk))
        entry = process_step.encyclopedia_entry
        return render(request, 'encyclopedia/encyclopedia.html', {
                'entries': entries,
                'entry': entry
        })

    return render(request,'encyclopedia/encyclopedia.html',{'entries': entries})

class ParticipationTypeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ParticipationTypeSerializer
    queryset = ParticipationType.objects.all()
