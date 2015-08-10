# -*- coding: utf-8 -*-
import json
from django.core.urlresolvers import reverse
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from wbc.region.serializers import DepartmentSerializer
from .models import *


class ProcessTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProcessType
        fields = ('id', 'name', 'description')


class ProcessStepSerializer(serializers.ModelSerializer):
    internal_link = serializers.SerializerMethodField(
        'internal_link_serializer_method')
    process_type = ProcessTypeSerializer()

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.process.views.process') + '#' + str(obj.id)

    class Meta:
        model = ProcessStep
        fields = ('id', 'name', 'description', 'icon', 'hover_icon',
                  'order', 'process_type', 'internal_link')


class PublicationSerializer(serializers.ModelSerializer):
    process_step = ProcessStepSerializer()
    department = DepartmentSerializer()

    class Meta:
        model = Publication
        fields = ('id', 'begin', 'end', 'office', 'office_hours',
                  'link', 'process_step', 'place', 'department')


class PlaceSerializer(serializers.ModelSerializer):
    point = serializers.SerializerMethodField('point_serializer_method')
    internal_link = serializers.SerializerMethodField(
        'internal_link_serializer_method')
    publications = PublicationSerializer(many=True)

    def point_serializer_method(self, obj):
        return [obj.lon, obj.lat]

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.process.views.place', args=[obj.id])

    class Meta:
        model = Place
        fields = ('id', 'point', 'identifier', 'address', 'description',
                  'entities', 'publications', 'link', 'internal_link')


class PlacePointSerializer(GeoFeatureModelSerializer):
    point = serializers.SerializerMethodField('point_serializer_method')
    internal_link = serializers.SerializerMethodField(
        'internal_link_serializer_method')
    publications = PublicationSerializer(many=True)

    def point_serializer_method(self, obj):
        return {'type': 'Point', 'coordinates': [obj.lon, obj.lat]}

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.process.views.place', args=[obj.id])

    class Meta:
        model = Place
        geo_field = 'point'
        fields = ('id', 'point', 'identifier', 'address', 'description',
                  'entities', 'publications', 'link', 'internal_link')


class PlacePolygonSerializer(GeoFeatureModelSerializer):

    polygon = serializers.SerializerMethodField('polygon_serializer_method')
    point = serializers.SerializerMethodField('point_serializer_method')
    internal_link = serializers.SerializerMethodField(
        'internal_link_serializer_method')
    publications = PublicationSerializer(many=True)

    def polygon_serializer_method(self, obj):
        if obj.polygon:
            return {'type': 'MultiPolygon', 'coordinates': json.loads(obj.polygon)}
        else:
            return {}

    def point_serializer_method(self, obj):
        return [obj.lon, obj.lat]

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.process.views.place', args=[obj.id])

    class Meta:
        model = Place
        geo_field = 'polygon'
        fields = ('id', 'polygon', 'identifier', 'address', 'description',
                  'entities', 'point', 'publications', 'link', 'internal_link')


class ListSerializer(serializers.ModelSerializer):
    entities = serializers.SerializerMethodField('entities_serializer_method')
    internal_link = serializers.SerializerMethodField(
        'internal_link_serializer_method')

    def entities_serializer_method(self, obj):
        return ', '.join([entity.name for entity in obj.entities.all()])

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.process.views.place', args=[obj.id])

    class Meta:
        model = Place
        fields = ('id', 'identifier', 'address', 'entities', 'internal_link')


class MapSerializer(serializers.ModelSerializer):
    point = serializers.SerializerMethodField('point_serializer_method')
    internal_link = serializers.SerializerMethodField(
        'internal_link_serializer_method')
    publication = serializers.SerializerMethodField(
        'publication_serializer_method')

    def point_serializer_method(self, obj):
        return [obj.lon, obj.lat]

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.process.views.place', args=[obj.id])

    def publication_serializer_method(self, obj):
        publications = obj.publications.all()
        if len(publications) > 0:
            last_publication = obj.publications.all()[0]
            return {
                'begin': last_publication.begin,
                'end': last_publication.end,
                'department': last_publication.department.name,
                'process_step': {
                    'id': last_publication.process_step.id,
                    'name': last_publication.process_step.name,
                    'internal_link': reverse('wbc.process.views.process') + '#' + str(last_publication.process_step.id),
                    'process_type': last_publication.process_step.process_type.name
                }
            }
        else:
            return {}

    class Meta:
        model = Place
        fields = ('id', 'point', 'identifier', 'address',
                  'entities', 'publication', 'internal_link')
