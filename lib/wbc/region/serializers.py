# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import *

class QuarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quarter

class DistrictSerializer(serializers.ModelSerializer):
    quarters = QuarterSerializer(many=True)

    class Meta:
        model = District
        fields = ('id','name','description','lat','lon','polygon','quarters')

class MuncipalitySerializer(serializers.ModelSerializer):

    districts = DistrictSerializer(many=True)

    class Meta:
        model = Muncipality
        fields = ('id','name','description','lat','lon','polygon','districts')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id','name','description','link','entity')
