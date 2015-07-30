# -*- coding: utf-8 -*-
import json
from django.core.urlresolvers import reverse
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from wbc.stakeholder.serializers import DepartmentSerializer
from models import *
from wbc.events.serializers import EventSerializer
from photologue.models import Gallery



class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('title','description','sample', 'date_added')

class ProjectSerializer(serializers.ModelSerializer):
    point = serializers.SerializerMethodField('point_serializer_method')
    internal_link = serializers.SerializerMethodField('internal_link_serializer_method')
    # events = EventSerializer(many=True)
    # gallery = GallerySerializer(many=True)
    
    def point_serializer_method(self, obj):
        return [obj.lon,obj.lat]

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.projects.views.projectslug',args=[obj.slug])

    # def gallery_serializer_method(self, obj):
    #     print obj.gallery
    #     return obj.gallery

    class Meta:
        model = Project
        fields = ('id','point','identifier','address','description','entities','events','link','internal_link', 'gallery')

class ProjectPointSerializer(GeoFeatureModelSerializer):
    point = serializers.SerializerMethodField('point_serializer_method')
    internal_link = serializers.SerializerMethodField('internal_link_serializer_method')
    # publications = publication_serializer_method(many=True)

    def point_serializer_method(self, obj):
        return {'type': 'Point', 'coordinates': [obj.lon,obj.lat]}

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.projects.views.project',args=[obj.id])

    class Meta:
        model = Project
        geo_field = 'point'
        fields = ('id','point','identifier','address','description','entities','link','internal_link')

class ProjectPolygonSerializer(GeoFeatureModelSerializer):

    polygon = serializers.SerializerMethodField('polygon_serializer_method')
    point = serializers.SerializerMethodField('point_serializer_method')
    internal_link = serializers.SerializerMethodField('internal_link_serializer_method')
    # publications = PublicationSerializer(many=True)

    def polygon_serializer_method(self, obj):
        if obj.polygon:
            return {'type': 'MultiPolygon', 'coordinates': json.loads(obj.polygon)}
        else:
            return {}

    def point_serializer_method(self, obj):
        return [obj.lon,obj.lat]

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.projects.views.project',args=[obj.id])

    class Meta:
        model = Project
        geo_field = 'polygon'
        fields = ('id','polygon','identifier','address','description','entities','point','link','internal_link')

class ListSerializer(serializers.ModelSerializer):
    entities = serializers.SerializerMethodField('entities_serializer_method')
    internal_link = serializers.SerializerMethodField('internal_link_serializer_method')

    def entities_serializer_method(self, obj):
        return ', '.join([entity.name for entity in obj.entities.all()])

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.projects.views.project',args=[obj.id])

    class Meta:
        model = Project
        fields = ('id','identifier','address','entities','internal_link')

class MapSerializer(serializers.ModelSerializer):
    point = serializers.SerializerMethodField('point_serializer_method')
    internal_link = serializers.SerializerMethodField('internal_link_serializer_method')
    # publication = serializers.SerializerMethodField('publication_serializer_method')

    def point_serializer_method(self, obj):
        return [obj.lon,obj.lat]

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.projects.views.projectslug',args=[obj.slug])

    # def publication_serializer_method(self, obj):
    #     publications = obj.publications.all()
    #     if len(publications) > 0:
    #         last_publication = obj.publications.all()[0]
    #         return {
    #             'begin': last_publication.begin,
    #             'end': last_publication.end,
    #             'department': last_publication.department.name,
    #             'process_step': {
    #                 'id': last_publication.process_step.id,
    #                 'name': last_publication.process_step.name,
    #                 'internal_link': reverse('wbc.projects.views.project') + '#' + str(last_publication.process_step.id),
    #                 'process_type': last_publication.process_step.process_type.name
    #             }
    #         }
    #     else:
    #         return {}

    class Meta:
        model = Project
        fields = ('id','point','identifier','address','entities','internal_link')

