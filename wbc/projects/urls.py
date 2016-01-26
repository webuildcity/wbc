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
    url(r'^(?P<pk>[0-9]+)/photo_upload/', 'wbc.projects.views.photo_upload', name="project_photo_upload"),
    url(r'^(?P<pk>[0-9]+)/photo_delete/(?P<photo>[0-9]+)', 'wbc.projects.views.photo_delete', name="project_photo_delete"),

)
