# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework import routers

from views import MapViewSet, ListViewSet, ProjectViewSet

router = routers.DefaultRouter()
router.register(r'list', ListViewSet, base_name='listitem')
router.register(r'map', MapViewSet, base_name='mapitem')

router.register(r'projects', ProjectViewSet, base_name='projects')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
