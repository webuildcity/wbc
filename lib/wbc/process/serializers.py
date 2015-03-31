# -*- coding: utf-8 -*-
import json
from django.core.urlresolvers import reverse
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from wbc.region.serializers import DepartmentSerializer
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

class InternalProcessStepSerializer(serializers.ModelSerializer):
    internal_link = serializers.SerializerMethodField('internal_link_serializer_method')
    process_type = serializers.SerializerMethodField('process_type_serializer_method')

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.process.views.process') + '#' + str(obj.id)

    def process_type_serializer_method(self, obj):
        return obj.process_type.name

    class Meta:
        model = ProcessStep
        fields = ('id','name','process_type','internal_link')

class PublicationSerializer(serializers.ModelSerializer):
    process_step_id = ProcessStepSerializer()
    department = DepartmentSerializer()

    class Meta:
        model = Publication
        fields = ('id','begin','end','office','office_hours','link','process_step','place','department')

class InternalPublicationSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField('department_serializer_method')
    process_step = InternalProcessStepSerializer()

    def department_serializer_method(self, obj):
        return obj.department.name

    class Meta:
        model = Publication
        fields = ('id','begin','end','process_step','department')

class PlaceSerializer(serializers.ModelSerializer):
    point = serializers.SerializerMethodField('point_serializer_method')
    internal_link = serializers.SerializerMethodField('internal_link_serializer_method')
    publications = PublicationSerializer(many=True)

    def point_serializer_method(self, obj):
        return [obj.lon,obj.lat]

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.process.views.place',args=[obj.id])

    class Meta:
        model = Place
        fields = ('id','point','identifier','address','description','entities','publications','link','internal_link')

class InternalPlaceSerializer(serializers.ModelSerializer):
    point = serializers.SerializerMethodField('point_serializer_method')
    internal_link = serializers.SerializerMethodField('internal_link_serializer_method')
    publications = InternalPublicationSerializer(many=True)

    def point_serializer_method(self, obj):
        return [obj.lon,obj.lat]

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.process.views.place',args=[obj.id])

    class Meta:
        model = Place
        fields = ('id','point','identifier','address','description','link','internal_link','publications')

class PlacePointSerializer(GeoFeatureModelSerializer):
    point = serializers.SerializerMethodField('point_serializer_method')
    internal_link = serializers.SerializerMethodField('internal_link_serializer_method')
    publications = PublicationSerializer(many=True)

    def point_serializer_method(self, obj):
        return {'type': 'Point', 'coordinates': [obj.lon,obj.lat]}

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.process.views.place',args=[obj.id])

    class Meta:
        model = Place
        geo_field = 'point'
        fields = ('id','point','identifier','address','description','entities','publications','link','internal_link')

class InternalPlacePointSerializer(GeoFeatureModelSerializer):

    point = serializers.SerializerMethodField('point_serializer_method')

    def point_serializer_method(self, obj):
        return {'type': 'Point', 'coordinates': [obj.lon,obj.lat]}

    class Meta:
        model = Place
        geo_field = 'point'
        fields = ('id','point')

class PlacePolygonSerializer(GeoFeatureModelSerializer):

    polygon = serializers.SerializerMethodField('polygon_serializer_method')
    point = serializers.SerializerMethodField('point_serializer_method')
    internal_link = serializers.SerializerMethodField('internal_link_serializer_method')
    publications = PublicationSerializer(many=True)

    def polygon_serializer_method(self, obj):
        if obj.polygon:
            return {'type': 'MultiPolygon', 'coordinates': json.loads(obj.polygon)}
        else:
            return {}

    def point_serializer_method(self, obj):
        return [obj.lon,obj.lat]

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.process.views.place',args=[obj.id])

    class Meta:
        model = Place
        geo_field = 'polygon'
        fields = ('id','polygon','identifier','address','description','entities','point','publications','link','internal_link')

class InternalPlacePolygonSerializer(GeoFeatureModelSerializer):

    polygon = serializers.SerializerMethodField('polygon_serializer_method')
    point = serializers.SerializerMethodField('point_serializer_method')

    def polygon_serializer_method(self, obj):
        if obj.polygon:
            return {'type': 'MultiPolygon', 'coordinates': json.loads(obj.polygon)}
        else:
            return {}

    def point_serializer_method(self, obj):
        return [obj.lon,obj.lat]

    class Meta:
        model = Place
        geo_field = 'polygon'
        fields = ('id','polygon','point')
