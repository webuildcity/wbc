# -*- coding: utf-8 -*-
from rest_framework import serializers

from models import *

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication

class ProcessStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessStep

class ProcessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessType
