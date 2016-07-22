# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from django.template import RequestContext
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from wbc.core.forms import LoginForm
from wbc.stakeholder.models import Stakeholder
from wbc.projects.models import Project
from wbc.region.models import District

from haystack.query import SearchQuerySet
from haystack.inputs import AutoQuery, Exact, Clean
from haystack.utils.geo import Point

from guardian.decorators import permission_required_or_403, permission_required
from guardian.mixins import PermissionRequiredMixin

from django_comments.views.comments import post_comment

def feeds(request):
    entities = District.objects.all()
    return render(request, 'core/feeds.html', {
        'entities': entities,
        'publication_feed_url': reverse('publication_feed_url')
    })


def login_user(request):

    email = ''
    if request.method == 'GET':
        email = request.GET.get('email', '')
    data = {'username' : email}
    form = LoginForm(request.POST or None, initial=data)

    if request.method == 'POST':
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                if request.POST.get('next'):
                    return JsonResponse({'redirect':  request.POST.get('next')})
                    # return HttpResponseRedirect(request.POST.get('next'))
                else:
                    # return HttpResponseRedirect('/')
                    return JsonResponse({'redirect':  '/'})

    return render(request, 'core/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))
    suggestions = []

    # return first 10 results
    for result in sqs[:10]:
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

class StartView(TemplateView):

    # template_name="core/startpage.html"

    def get_context_data(self, **kwargs):
        now = datetime.now()
        context = super(StartView, self).get_context_data(**kwargs)
        # context['latest'] = 
        projects = Project.objects.filter(events__begin__gte=now)[:3]
        context['upcoming'] = projects
        context['topIcons'] = settings.STARTPAGE_OVERVIEW_ICONS;
        context['botIcons'] = settings.STARTPAGE_TOPIC_ICONS;
        return context
        
class SearchView(TemplateView):

    template_name = "core/search.html"
    
    # terminated_process = ProcessStep.
    def search(self, data):
        sqs = SearchQuerySet().facet('tags').facet('entities')
        model_dict = {
            'project' : Project,
#            'stakeholder': Stakeholder 
        }
        offset = 0

        suggestions = sqs.spelling_suggestion()
        # Disable finished projects by default
        if 'terminated' in data and data['terminated'] == True:
            pass
        else:
            sqs = sqs.exclude(isFinished=True)
        
        if 'buffer_areas' in data and data['buffer_areas']:
            sqs = sqs.filter(_exists_="buffer_areas")
        
        if 'bounds' in data:
            bl = Point(data['bounds']['_southWest']['lat'], data['bounds']['_southWest']['lng'])
            tr = Point(data['bounds']['_northEast']['lat'], data['bounds']['_northEast']['lng'])
            sqs = sqs.within('location', bl, tr)
              
        if 'q' in data:
            if data['q'] != "":
                sqs = sqs.filter(content=AutoQuery(data['q']))
        
        # print suggestions

        if 'models' in data:
            for model in data['models']:
                sqs = sqs.models(model_dict[model])

        if 'tags' in data:
            # see ff string or array is parsed
            if len(data['tags']) >0:
                for tag in data['tags']:
                    sqs = sqs.filter(tags__name__in=[tag])

        if 'entities' in data:
            if len(data['entities']) >0:
                sqs = sqs.filter(entities__name__in=data['entities'])
        
        if 'order' in data:
            if data['order'] != '' and data['order'] != '-':
                order = data['order']
                sqs = sqs.order_by(order)

        if 'offset' in data:
            offset = data['offset']
            if data['offset'] == -1:
                sqs_copy = sqs
            else:
                sqs_copy = sqs[offset:offset+50]
        else:
            sqs_copy = sqs[offset:offset+50]

        results = []
        for result in sqs_copy:
            terminated = None
            if result.finished:
                terminated = result.finished.strftime("%d.%m.%y")
            resultdict = dict(name=result.name, pk=result.pk, type=result.type, internal_link=result.internal_link, address_obj=result.address_obj, thumbnail=result.thumbnail, num_stakeholder=result.num_stakeholder, created=result.created.strftime("%d.%m.%y"), created_by=result.created_by, teaser=result.teaser, ratings_count=result.ratings_count, ratings_avg=result.ratings_avg, buffer_areas=result.buffer_areas, finished=terminated, isFinished=result.isFinished)
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
            'suggestion': suggestions
        })
        return data

    def get(self, request):
        query =  request.GET.urlencode()
        q = request.GET.get('q', '')
        return render(request, 'core/search.html',  context={'q': q, 'order_btns' : settings.ORDER_BTNS, 'mapview' : settings.DEFAULT_VIEW_MAP})

    def post(self, request):
        data = json.loads(request.body)
        data = self.search(data);
        return HttpResponse(data, content_type='application/json')
    
def map(request):
    return render(request, 'core/map_page.html')


class ProtectedCreateView(CreateView):

    def dispatch(self, request, *args, **kwargs):
      #  print '%s.1add_%s' % (self.model._meta.app_label, self.model._meta.model_name)
        @permission_required_or_403('%s.add_%s' % (self.model._meta.app_label, self.model._meta.model_name), accept_global_perms=True)
        def wrapper(request, *args, **kwargs):
            return super(ProtectedCreateView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)

class ProtectedUpdateView(UpdateView):      

    def dispatch(self, request, *args, **kwargs):
        modelString = '%s.%s' % (self.model._meta.app_label, self.model._meta.model_name)
        @permission_required_or_403('%s.change_%s' % (self.model._meta.app_label, self.model._meta.model_name), (modelString, 'pk', 'pk'), accept_global_perms=True)
        def wrapper(request, *args, **kwargs):
            return super(ProtectedUpdateView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)

class ProtectedDeleteView(DeleteView):

    def dispatch(self, request, *args, **kwargs):
        modelString = '%s.%s' % (self.model._meta.app_label, self.model._meta.model_name)
        @permission_required_or_403('%s.delete_%s' % (self.model._meta.app_label, self.model._meta.model_name), (modelString, 'pk', 'pk'), accept_global_perms=True)
        def wrapper(request, *args, **kwargs):
            return super(ProtectedDeleteView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)

def comment_post_wrapper(request):
    # Clean the request to prevent form spoofing
    if request.user.is_authenticated():
        if not (request.user.get_full_name() == request.POST['name'] or \
               request.user.email == request.POST['email']):
            return HttpResponse("Nice try!")
        return post_comment(request)
    return HttpResponse("Nice try!")
