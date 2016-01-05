# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework import routers
from views import *

router = routers.DefaultRouter()
router.register(r'events', EventViewSet, base_name='event')
router.register(r'dates', DateViewSet, base_name='date')
router.register(r'media_api', MediaViewSet, base_name='media')
router.register(r'publications', PublicationViewSet, base_name='publication')


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
        # veroeffentlichungen neu
    url(r'^neu/(?P<project_pk>[0-9]+)/$', EventCreate.as_view(), name='event_create'),
    url(r'^(?P<pk>[0-9]+)/bearbeiten/(?P<project_pk>[0-9]+)/$', EventUpdate.as_view(), name='event_update'),
    url(r'^(?P<pk>[0-9]+)/entfernen/(?P<project_pk>[0-9]+)/$', EventDelete.as_view(), name='event_delete'),
    url(r'^date/neu/(?P<project_pk>[0-9]+)$', DateCreate.as_view(), name='date_create'),
    url(r'^date/(?P<pk>[0-9]+)/bearbeiten/(?P<project_pk>[0-9]+)/$', DateUpdate.as_view(), name='date_update'),
    url(r'^date/(?P<pk>[0-9]+)/entfernen/(?P<project_pk>[0-9]+)/$', DateDelete.as_view(), name='date_delete'),
    url(r'^media/neu/(?P<project_pk>[0-9]+)/$', MediaCreate.as_view(), name='media_create'),
    url(r'^media/(?P<pk>[0-9]+)/bearbeiten/(?P<project_pk>[0-9]+)/$', MediaUpdate.as_view(), name='media_update'),
    url(r'^media/(?P<pk>[0-9]+)/entfernen/(?P<project_pk>[0-9]+)/$', MediaDelete.as_view(), name='media_delete'),
    url(r'^pub/neu/(?P<project_pk>[0-9]+)/$', PubCreate.as_view(), name='pub_create'),
    url(r'^pub/(?P<pk>[0-9]+)/bearbeiten/(?P<project_pk>[0-9]+)/$', PubUpdate.as_view(), name='pub_update'),
    url(r'^pub/(?P<pk>[0-9]+)/entfernen/(?P<project_pk>[0-9]+)/$', PubDelete.as_view(), name='pub_delete'),
)
