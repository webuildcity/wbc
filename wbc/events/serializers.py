# -*- coding: utf-8 -*-
from rest_framework import serializers

from models import *

class EventSerializer(serializers.ModelSerializer):
    # def to_representation(self, value):
    #     if isinstance(value, Date):
    #         print "date"
    #     if isinstance(value, Media):
    #         print "media"
    #     if isinstance(value, Event):
    #         print "event"
    class Meta:
        model = Event
        fields = ('title','description','link')

class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ('title','description','link')

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('title','description','link')

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('title','description','link')