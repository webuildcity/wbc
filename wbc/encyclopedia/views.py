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


class EncyclopediaEntryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EncyclopediaEntrySerializer
    queryset = EncyclopediaEntry.objects.filter()

def encyclopedia(request, pk=None):
    entries = EncyclopediaEntry.objects.all()
    if pk:
        entry = get_object_or_404(EncyclopediaEntry, pk=int(pk))
        return render(request, 'encyclopedia/encyclopedia.html', {
                'entries': entries,
                'selected_entry': entry
        })

    return render(request,'encyclopedia/encyclopedia.html',{'entries': entries})
