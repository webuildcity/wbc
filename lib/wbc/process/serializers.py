# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from wbc.region.serializers import DistrictSerializer,DepartmentSerializer
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

class PublicationSerializer(serializers.ModelSerializer):
    process_step = ProcessStepSerializer()
    department = DepartmentSerializer()
    class Meta:
        model = Publication
        fields = ('id','begin','end','office','office_hours','link','process_step','place','department')

class PlaceSerializer(GeoFeatureModelSerializer):

    point = serializers.SerializerMethodField('point_serializer_method')
    internal_link = serializers.SerializerMethodField('internal_link_serializer_method')
    publications = PublicationSerializer(many=True)

    def point_serializer_method(self, obj):
        return {'type': 'point', 'coordinates': [obj.lon,obj.lat]}

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.process.views.place',args=[obj.id])

    class Meta:
        model = Place
        geo_field = 'point'
        fields = ('id','identifier','address','description','entities','point','publications','link','internal_link')
