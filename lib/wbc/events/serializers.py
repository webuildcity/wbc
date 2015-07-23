# -*- coding: utf-8 -*-
from rest_framework import serializers

from models import *

class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name','address','description','link')

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ('firstName','lastName','address','description','link')

class Process_bplanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ('firstName','lastName','address','description','link')