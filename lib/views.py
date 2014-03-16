from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.views.decorators.csrf import csrf_exempt
import django.views.generic

import json

class View(django.views.generic.View):
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
