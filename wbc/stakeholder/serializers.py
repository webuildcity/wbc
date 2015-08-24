# -*- coding: utf-8 -*-
from rest_framework import serializers

from models import *

class StakeholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stakeholder
        fields = ('name','address','description')

class StakeholderRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StakeholderRole
        fields = ('role','description')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id','name','description','link','entity')