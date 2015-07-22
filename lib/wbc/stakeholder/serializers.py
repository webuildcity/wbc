# -*- coding: utf-8 -*-
from rest_framework import serializers

from models import *

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('name','address','description','link')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('firstName','lastName','address','description','link')