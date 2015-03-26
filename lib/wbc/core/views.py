# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.contrib.auth import login, logout
from django.template import RequestContext

from wbc.core.forms import LoginForm

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
    return render(request, 'core/login.html', {'form': form })

def logout_user(request):
    logout(request)
    return render_to_response('core/logout.html', context_instance=RequestContext(request))
