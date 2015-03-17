# -*- coding: utf-8 -*-
import datetime,json

from django.views.generic import View as GenericView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import Http404,render_to_response,redirect,render,get_object_or_404
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.conf import settings
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from django.template import RequestContext

from wbc.core.forms import LoginForm,FindOrt,CreateVeroeffentlichung
from wbc.projects.models import Ort, Veroeffentlichung, Verfahrensschritt, Verfahren, Behoerde, Bezirk
from wbc.comments.models import Kommentar
from wbc.comments.forms import  KommentarForm

class View(GenericView):
    http_method_names = ['get']

    def dispatch(self, request, *args, **kwargs):
        # get the accept header
        if 'HTTP_ACCEPT' in request.META:
            accept = request.META['HTTP_ACCEPT'].split(',')
        else:
            accept = ''

        if request.GET.get('format') == 'json' or 'application/json' in accept:
            self.accept = 'json'
        else:
            self.accept = 'html'

        return super(View,self).dispatch(request, *args, **kwargs)

    def get(self, request, pk=None):
        if pk:
            return self.get_object(request,pk)
        else:
            return self.get_objects(request)

    def render(self, request, template, context):
        if self.accept == 'json':
            jsonDict = self.constructJsonDict(context)
            return HttpResponse(json.dumps(jsonDict,cls=DjangoJSONEncoder),content_type="application/json")
        else:
            return render(request,template,context)

    def constructJsonDict(self, context):
        jsonDict = {}
        for key in context:
            element = context[key]

            if isinstance(element, models.query.QuerySet):
                # the element is a django query set and needs to be serialized
                jsonDict[key] = []
                for row in serializers.serialize("python", element):
                    row['fields'].update({'pk': row['pk']})
                    jsonDict[key].append(row['fields'])

            elif isinstance(element, models.Model):
                # the element is a django model and needs to be serialized
                dictionary = serializers.serialize("python", [element])[0]
                jsonDict[key] = dictionary['fields']
                jsonDict[key]['pk'] = dictionary['pk']

            else:
                # the element is just a normal django dictionary
                jsonDict[key] = element

        return jsonDict

    class Meta:
        abstract = True

def home(request):
    return render(request,'core/map.html')

def orte(request):
    orte = Ort.objects.all()
    return render(request,'core/orte.html', {'orte': orte})

def ort(request,pk):
    ort = get_object_or_404(Ort, id = int(pk))
    if request.method == 'POST':
        if len(request.POST["author_email1"]) == 0:
            kommentar_neu = KommentarForm(request.POST)
            if kommentar_neu.is_valid():
                kommentar = kommentar_neu.save(commit=False)
                kommentar.enabled = True;
                kommentar.ort = ort
                kommentar.save()

    kommentare = Kommentar.objects.filter(ort_id = int(pk), enabled = True)
    return render(request, 'core/ort.html', {'ort': ort, 'kommentare': kommentare})

def begriffe(request):
    verfahren = Verfahren.objects.all()
    return render(request,'core/begriffe.html',{'verfahren': verfahren})

def feeds(request):
    bezirke = Bezirk.objects.all()
    return render(request,'core/feeds.html',{'bezirke': bezirke})

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

@login_required
def create_veroeffentlichung(request):
    orte_id = request.GET.get('orte_id', None)

    if orte_id == None:
        form = FindOrt()
        return render(request, 'core/create_veroeffentlichung_step1.html', {'form':form})

    else:
        ort = Ort.objects.get(pk=orte_id)

        if request.method == 'POST':
            form = CreateVeroeffentlichung(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/orte/' + str(ort.pk))
            else:
                return render(request, 'core/create_veroeffentlichung_step2.html', {'form':form})
        else:
            form = CreateVeroeffentlichung(initial={'ort': ort})
            return render(request,'core/create_veroeffentlichung_step2.html',{'form':form})

class VeroeffentlichungenFeedMimeType(Rss201rev2Feed):
    mime_type = 'application/xml'

class VeroeffentlichungenFeed(Feed):
    title = "Bürger baut Stadt (Veröffentlichungen)"
    description = "Veröffentlichungen zu Bauvorhaben in Berlin"
    link = settings.SITE_URL
    feed_url = settings.SITE_URL + "/veroeffentlichungen/feed/"
    feed_type = VeroeffentlichungenFeedMimeType

    def get_object(self, request):
        if 'bezirk' in request.GET:
            bezirk = request.GET['bezirk']
            try:
                Bezirk.objects.get(name=bezirk)
            except Bezirk.DoesNotExist:
                raise Http404
            return Veroeffentlichung.objects.filter(ort__bezirke__name=bezirk)
        return Veroeffentlichung.objects

    def items(self, objs):
        return objs.order_by('-created')[:10]

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
