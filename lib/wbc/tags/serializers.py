# -*- coding: utf-8 -*-
from rest_framework import serializers

from models import *

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name','description','other')

