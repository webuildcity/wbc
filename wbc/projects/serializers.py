# -*- coding: utf-8 -*-
import json
from django.core.urlresolvers import reverse
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from wbc.stakeholder.serializers import DepartmentSerializer
from models import *
from wbc.events.serializers import EventSerializer
from wbc.images.serializers import AlbumSerializer

class ProjectSerializer(serializers.ModelSerializer):
    point = serializers.SerializerMethodField('point_serializer_method')
    internal_link = serializers.SerializerMethodField('internal_link_serializer_method')
    # events = serializers.RelatedField(read_only='True')
    # gallery = GallerySerializer(many=True)

    last_news = serializers.SerializerMethodField('last_news_serializer')
    next_date = serializers.SerializerMethodField('next_date_serializer')
    album = serializers.SerializerMethodField('album_serializer')
    
    def point_serializer_method(self, obj):
        return [obj.lon,obj.lat]

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.projects.views.projectslug',args=[obj.slug])

    def last_news_serializer(self,obj):
        date = obj.get_last_news()
        if date:
            return EventSerializer(date).data
        return None
    
    def next_date_serializer(self,obj):
        date = obj.get_next_date()
        if date:
            return EventSerializer(date).data
        return None

    def album_serializer(self, obj):
        album = obj.album
        if album:
            return AlbumSerializer(album).data
        return None
    
    class Meta:
        model = Project
        fields = ('id','name','point', 'events','identifier','address','description','entities','link','internal_link', 'album', 'last_news', 'next_date', 'date_string')
        depth = 1

class ProjectPointSerializer(serializers.ModelSerializer):
    point = serializers.SerializerMethodField('point_serializer_method')
    internal_link = serializers.SerializerMethodField('internal_link_serializer_method')
    # publications = publication_serializer_method(many=True)

    def point_serializer_method(self, obj):
        return obj.point_gis.geojson

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.projects.views.projectslug',args=[obj.slug])

    class Meta:
        model = Project
        # geo_field = 'point'
        fields = ('id','point','identifier','address','description','entities','link','internal_link')

class ProjectPolygonSerializer(serializers.ModelSerializer):

    point = serializers.SerializerMethodField('point_serializer_method')
    internal_link = serializers.SerializerMethodField('internal_link_serializer_method')
    # publications = PublicationSerializer(many=True)

    # def polygon_serializer_method(self, obj):
    #     return obj.polygon_gis

    def point_serializer_method(self, obj):
        return [obj.lon,obj.lat]

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.projects.views.projectslug',args=[obj.slug])

    class Meta:
        model = Project
        geo_field = 'polygon_gis'
        fields = ('id','polygon_gis','identifier','address','description','entities','point','link','internal_link')

class ListSerializer(serializers.ModelSerializer):
    entities = serializers.SerializerMethodField('entities_serializer_method')
    internal_link = serializers.SerializerMethodField('internal_link_serializer_method')

    def entities_serializer_method(self, obj):
        return ', '.join([entity.name for entity in obj.entities.all()])

    def internal_link_serializer_method(self, obj):
        return reverse('wbc.projects.views.projectslug',args=[obj.slug])

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

