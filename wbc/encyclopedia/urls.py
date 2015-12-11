# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register(r'encyclopediaentries', EncyclopediaEntryViewSet, base_name='encyclopediaentry')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
