# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponseRedirect
from projects.models import Ort, Veroeffentlichung, Verfahrensschritt, Verfahren, Behoerde, Bezirk
from bbs.forms import LoginForm
from django.shortcuts import Http404,render_to_response,redirect,render
from django.contrib.auth import authenticate, login, logout
from bbs.forms import FindOrt,CreateVeroeffentlichung
from django.template import RequestContext
import datetime
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'bbs/map.html')

def orte(request):
    orte = Ort.objects.all()
    return render(request,'bbs/orte.html', {'orte': orte})

def ort(request,pk):
    try:
        ort = Ort.objects.get(pk=int(pk))
    except Ort.DoesNotExist:
        raise Http404
    return render(request, 'bbs/ort.html', {'ort': ort})

def begriffe(request):
    verfahren = Verfahren.objects.all()
    return render(request,'bbs/begriffe.html',{'verfahren': verfahren})  

def login_user(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                if request.GET.get('next'):
                    return HttpResponseRedirect(request.GET.get('next'))# Redirect to a success page.
                else:
                    return HttpResponseRedirect('/')
    return render(request, 'bbs/login.html', {'form': form })

def logout_user(request):
    logout(request)
    return render_to_response('bbs/logout.html', context_instance=RequestContext(request))

@login_required
def create_veroeffentlichung(request):
    orte_id = request.GET.get('orte_id', None)

    if orte_id == None:
        form = FindOrt()
        return render(request, 'bbs/create_veroeffentlichung_step1.html', {'form':form})

    else:
        ort = Ort.objects.get(pk=orte_id)

        if request.method == 'POST': 
            form = CreateVeroeffentlichung(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/orte/' + str(ort.pk))
            else:
                return render(request, 'bbs/create_veroeffentlichung_step2.html', {'form':form})
        else:
            form = CreateVeroeffentlichung(initial={'ort': ort})
            return render(request,'bbs/create_veroeffentlichung_step2.html',{'form':form})
