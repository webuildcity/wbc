from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
import json

from django.views.generic import View

class RestView(View):

    def dispatch(self, request, *args, **kwargs):
        
        # set accept variable from http accept header
        if 'application/xhtml+xml' in request.META['HTTP_ACCEPT'].split(','):
            self.accept = 'html'
        elif 'application/json' in request.META['HTTP_ACCEPT'].split(','):
            self.accept = 'json'
        else:
            raise RuntimeError('An error has occured')

        # call method determined by http proverb
        if 'pk' in kwargs:
            if request.method == 'GET':
                return self.get_item(request, *args, **kwargs)
            elif request.method == 'POST':
                return self.post_item(request, *args, **kwargs)
            elif request.method == 'PUT':
                return self.put_item(request, *args, **kwargs)
            elif request.method == 'DELETE':
                return self.delete_item(request, *args, **kwargs)
        else:
            if request.method == 'GET':
                return self.get_items(request, *args, **kwargs)
            elif request.method == 'POST':
                return self.post_items(request, *args, **kwargs)
            elif request.method == 'PUT':
                return self.put_items(request, *args, **kwargs)
            elif request.method == 'DELETE':
                return self.delete_items(request, *args, **kwargs)

    def render(self, request, template, response):
        if self.accept == 'json':
            jsonDict = {}
            for key in response:
                element = response[key]

                if isinstance(element, models.query.QuerySet):
                    jsonDict[key] = serializers.serialize("python", element)
                elif isinstance(element, models.Model):
                    jsonDict[key] = serializers.serialize("python", [element])[0]
                else:
                    jsonDict[key] = element

            return HttpResponse(json.dumps(jsonDict, cls=DjangoJSONEncoder), content_type="application/json")
        else:
            return render(request, template, response)
