from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.views.decorators.csrf import csrf_exempt
import django.views.generic

import json

class View(django.views.generic.View):

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

    def serialiseResponse(response):
        dictionary = {}
        for key in response:
            element = response[key]
            if isinstance(element, models.query.QuerySet):
                dictionary[key] = []
                obj = serializers.serialize("python", element)
                for e in obj:
                    d = e['fields']
                    d['pk'] = e['pk']
                    dictionary[key].append(d)
            elif isinstance(element, models.Model):
                d = serializers.serialize("python", [element])[0]
                dictionary[key] =  d['fields']
                dictionary[key]['pk'] =  d['pk']
            else:
                dictionary[key] = element

        return dictionary
        
    def renderJson(self, request, response):
        return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder),
                            content_type="application/json")
    class Meta:
        abstract = True
