# -*- coding: utf-8 -*-
from rest_framework import serializers

from models import *

class MuncipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Muncipality

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District

class QuarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quarter

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department