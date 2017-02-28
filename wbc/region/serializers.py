# -*- coding: utf-8 -*-
from rest_framework import serializers
from wbc.projects.models import Project
from .models import *

class QuarterSerializer(serializers.ModelSerializer):

    denkmal_count = serializers.SerializerMethodField('denkmal_count_serializer_method')

    def denkmal_count_serializer_method(self,obj):
        denkmal_count = Project.objects.filter(quarter=obj.name).count()
        print denkmal_count
        return denkmal_count

    class Meta:
        model = Quarter
        fields = ('id', 'name', 'polygon', 'denkmal_count')

class DistrictSerializer(serializers.ModelSerializer):

    QuarterSerializer(many=True)

    class Meta:
        model = District
        fields = ('id','name','description','lat','lon','polygon','quarters')

class MuncipalitySerializer(serializers.ModelSerializer):

    districts = DistrictSerializer(many=True)

    class Meta:
        model = Muncipality
        fields = ('id','name','description','lat','lon','polygon','districts')