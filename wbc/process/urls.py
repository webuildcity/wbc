# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'list', ListViewSet, base_name='listitem')
router.register(r'map', MapViewSet, base_name='mapitem')

router.register(r'places', PlaceViewSet, base_name='place')
router.register(r'publications', PublicationViewSet, base_name='publication')
router.register(r'processsteps', ProcessStepViewSet, base_name='processstep')
router.register(r'processtypes', ProcessTypeViewSet, base_name='processtype')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
