# -*- coding: utf-8 -*-
import json,time,datetime

from django.http import HttpResponse
from django.shortcuts import Http404, render
from django.db.models import Q
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt

from wbc.projects.models import Ort, Veroeffentlichung, Verfahrensschritt, Verfahren, Behoerde, Bezirk


