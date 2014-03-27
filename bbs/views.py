# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponseRedirect
from projects.models import Ort, Veroeffentlichung, Verfahrensschritt, Verfahren, Behoerde, Bezirk
from bbs.forms import LoginForm
from django.shortcuts import render_to_response,redirect,render
from django.contrib.auth import authenticate, login, logout

from django.template import RequestContext
import datetime

def home(request):
    return render(request,'bbs/map.html')

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
