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
    url(r'^(?P<pk>[0-9]+)/subscribe/', 'wbc.projects.views.subscribe', name="project_subscribe"),
    url(r'^(?P<pk>[0-9]+)/blacklist/(?P<user>[0-9]+)', 'wbc.projects.views.blacklist', name="project_blacklist"),
    url(r'^(?P<pk>[0-9]+)/updownvote/(?P<vote>[0-9]+)', 'wbc.projects.views.updownvote', name="project_updownvote"),
    url(r'^(?P<pk>[0-9]+)/wbc_rate/(?P<user>[0-9]+)/(?P<tag>[a-zA-Z0-9_.-]+)', 'wbc.projects.views.wbc_rate', name="project_wbc_rate"),
    url(r'^(?P<pk>[0-9]+)/feature/', 'wbc.projects.views.feature', name="project_feature"),
    url(r'^(?P<pk>[0-9]+)/photo_delete/(?P<photo>[0-9]+)', 'wbc.projects.views.photo_delete', name="project_photo_delete"),

)
