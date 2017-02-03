# -*- coding: utf-8 -*-
from rest_framework import serializers

from models import *

class BaseStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseStep
        fields = ('identifier', 'bounds', 'imageBounds', 'cameraOptions', 'data', 'time', 'typeName', 'name', 'text', 'lat', 'lng', 'image', 'keepImg', 'keepText', 'fullText', 'audio', 'wms')


class SubstepSerializer(serializers.ModelSerializer):
    
    # text = serializers.SerializerMethodField('text_serializer')

    # def text_serializer(self, obj):
    #     if obj.text:
    #         return obj.text
    #     else:
    #         return None
    class Meta:
        model = Substep
        fields = ('identifier', 'bounds', 'imageBounds', 'cameraOptions', 'data', 'time', 'typeName', 'name', 'text', 'lat', 'lng', 'image', 'keepImg', 'keepText', 'fullText', 'audio', 'wms')


class AnchorSerializer(serializers.ModelSerializer):
    steps = SubstepSerializer(many=True, read_only=True)

    class Meta:
        model = Anchor
        fields = ('headline', 'identifier', 'bounds', 'imageBounds', 'cameraOptions', 'data', 'steps', 'time', 'typeName', 'name', 'text', 'lat', 'lng', 'image', 'keepImg', 'keepText', 'fullText', 'audio', 'wms')


class StorySerializer(serializers.ModelSerializer):
    anchors = AnchorSerializer(many=True, read_only=True)
    
    class Meta:
        model = Story
        fields = ('name', 'pk', 'description', 'subtitle', 'image', 'explanation', 'anchors')

class StoryListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Story
        fields = ('name','pk','description','subtitle', 'image', 'explanation')
