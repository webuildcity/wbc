# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout
from django.template import RequestContext

from wbc.core.forms import LoginForm
from wbc.region.models import District

def feeds(request):
    entities = District.objects.all()
    return render(request,'core/feeds.html',{
        'entities': entities,
        'publication_feed_url': reverse('publication_feed_url')
    })

def login_user(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                if request.GET.get('next'):
                    # Redirect to a success page.
                    return HttpResponseRedirect(request.GET.get('next'))
                else:
                    return HttpResponseRedirect('/')

    return render(request, 'core/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return render_to_response('core/logout.html', context_instance=RequestContext(request))
