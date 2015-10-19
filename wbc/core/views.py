# -*- coding: utf-8 -*-

import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from wbc.core.forms import LoginForm
from wbc.stakeholder.models import Stakeholder
from wbc.projects.models import Project
from wbc.region.models import District

from haystack.query import SearchQuerySet
from haystack.inputs import AutoQuery, Exact, Clean

def feeds(request):
    entities = District.objects.all()
    return render(request, 'core/feeds.html', {
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
                if request.POST.get('next'):
                    return HttpResponseRedirect(request.POST.get('next'))
                else:
                    return HttpResponseRedirect('/')

    return render(request, 'core/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return render_to_response('core/logout.html', context_instance=RequestContext(request))


def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))
    suggestions = []
    for result in sqs:
        resultdict = dict(name=result.name, pk=result.pk, type=result.type, internal_link=result.internal_link)
        if result.location:
            resultdict['location'] = [result.location[0], result.location[1]]

        if result.polygon:
            resultdict['polygon'] = json.loads(result.polygon)

        suggestions.append(resultdict)

    # suggestions = [dict(location=result.location, name=result.name) for result in sqs]
    data = json.dumps({
        'results': suggestions
    })
    return HttpResponse(data, content_type='application/json')

def search(request):
    data = json.loads(request.body)
    sqs = SearchQuerySet().facet('tags').facet('entities')
    model_dict = {
        'project' : Project,
        'stakeholder': Stakeholder 
    }
    offset = 0

    if 'offset' in data:
        offset = data['offset'] 
    
    if 'currentSearchTerm' in data:
        if data['currentSearchTerm'] != "":
            sqs = sqs.filter(content=AuyatoQuery(data['currentSearchTerm']))
    
    if 'models' in data:
        for model in data['models']:
            sqs = sqs.models(model_dict[model])

    if 'tags' in data:
        if len(data['tags']) >0:
            sqs = sqs.filter(tags__name__in=data['tags'])

    if 'entities' in data:
        if len(data['entities']) >0:
            sqs = sqs.filter(entities__name__in=data['entities'])
        

    results = []

    for result in sqs[:offset+20]:
        resultdict = dict(name=result.name, pk=result.pk, type=result.type, internal_link=result.internal_link)
        if result.location:
            resultdict['location'] = [result.location[0], result.location[1]]

        if result.polygon:
            resultdict['polygon'] = json.loads(result.polygon)

        results.append(resultdict)

    # suggestions = [dict(location=result.location, name=result.name) for result in sqs]
    data = json.dumps({
        'results': results,
        'length': len(sqs),
        'facets' : sqs.facet_counts(),
        'suggestion': sqs.spelling_suggestion()
    })
    return HttpResponse(data, content_type='application/json')

class ProtectedCreateView(CreateView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedCreateView, self).dispatch(*args, **kwargs)


class ProtectedUpdateView(UpdateView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedUpdateView, self).dispatch(*args, **kwargs)


class ProtectedDeleteView(DeleteView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedDeleteView, self).dispatch(*args, **kwargs)
