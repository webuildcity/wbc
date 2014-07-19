# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import Http404,render_to_response,redirect,render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from django.template import RequestContext

from forms import LoginForm,FindOrt,CreateVeroeffentlichung
from projects.models import Ort, Veroeffentlichung, Verfahrensschritt, Verfahren, Behoerde, Bezirk

import datetime,json

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

class VeroeffentlichungenFeedMimeType(Rss201rev2Feed):
    mime_type = 'application/xml'

class VeroeffentlichungenFeed(Feed):
    title = "Bürger baut Stadt (Veröffentlichungen)"
    description = "Veröffentlichungen zu Bauvorhaben in Berlin"
    link = settings.SITE_URL
    feed_url = settings.SITE_URL + "/veroeffentlichungen/feed/"
    feed_type = VeroeffentlichungenFeedMimeType

    def items(self):
        return Veroeffentlichung.objects.order_by('-created')[:10]

    def item_title(self, item):
        return item.verfahrensschritt.verfahren.name + ': ' +  item.verfahrensschritt.name + ' (' + item.ort.bezeichner + ', ' + item.ort.bezirke.all()[0].name + ')'

    def item_description(self, item):
        return item.beschreibung

    def item_guid(self, item):
        return str(item.pk)

    def item_pubdate(self, item):
        return item.created

    def item_link(self, item):
        return settings.SITE_URL + '/orte/' + str(item.ort.pk)