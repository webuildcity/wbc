# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponseRedirect
from projects.models import Ort, Veroeffentlichung, Verfahrensschritt, Verfahren, Behoerde, Bezirk
from bbs.forms import LoginForm, VeroeffentlichungForm, OrtForm
from django.shortcuts import Http404,render_to_response,redirect,render
from django.contrib.auth import authenticate, login, logout

from django.template import RequestContext
import datetime

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

def new_publication(request):

    vform = VeroeffentlichungForm()
    oform = OrtForm() 
    return render(request,'bbs/new.html',{'vform': vform, 'oform': oform}) 
    

