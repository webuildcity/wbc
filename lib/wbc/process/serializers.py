# -*- coding: utf-8 -*-
import json
from django.core.urlresolvers import reverse
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from wbc.stakeholder.serializers import DepartmentSerializer
from models import *

class ProcessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessType
        fields = ('id','name','description')

class ProcessStepSerializer(serializers.ModelSerializer):
    internal_link = serializers.SerializerMethodField('internal_link_serializer_method')
    process_type = ProcessTypeSerializer()

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.process.views.process') + '#' + str(obj.id)

    class Meta:
        model = ProcessStep
        fields = ('id','name','description','icon','hover_icon','order','process_type','internal_link')