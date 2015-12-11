# -*- coding: utf-8 -*-
import json
from django.core.urlresolvers import reverse
from rest_framework import serializers

from .models import *


class EncyclopediaEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = EncyclopediaEntry
        fields = ('id', 'title', 'gist', 'body_text', 'order', 'parent_entry')
