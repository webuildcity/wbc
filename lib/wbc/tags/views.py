# -*- coding: utf-8 -*-
from rest_framework import viewsets

from models import *
from serializers import *

class TagViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()