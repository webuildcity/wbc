# -*- coding: utf-8 -*-
import json
from django.core.urlresolvers import reverse
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import *


class ProcessTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProcessType
        fields = ('id', 'name', 'encyclopedia_entry', 'description')

class ParticipationTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParticipationType
        fields = ('id', 'name', 'description', 'encyclopedia_entry', 'participation', 'icon')

class ProcessStepSerializer(serializers.ModelSerializer):
    internal_link = serializers.SerializerMethodField(
        'internal_link_serializer_method')
    process_type = ProcessTypeSerializer()

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.process.views.process') + '#' + str(obj.id)

    class Meta:
        model = ProcessStep
        fields = ('id', 'name', 'description', 'encyclopedia_entry', 'icon', 'hover_icon',
                  'order', 'process_type', 'participation_type', 'parent_step',
                  'internal_link')
