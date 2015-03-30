# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from models import *

class PlaceSerializer(GeoFeatureModelSerializer):

    point = serializers.SerializerMethodField('point_serializer_method')

    def point_serializer_method(self, obj):
        return {'type': 'point', 'coordinates': [obj.lat,obj.lon]}

    class Meta:
        depth = 1
        model = Place
        geo_field = 'point'
        fields = ('id','identifier','address','description','entities','point')

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication

class ProcessStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessStep

class ProcessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessType
