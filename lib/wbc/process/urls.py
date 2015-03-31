# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework import routers

from views import *

router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet, base_name='place')
router.register(r'publications', PublicationViewSet, base_name='publication')
router.register(r'processsteps', ProcessStepViewSet, base_name='process_step')
router.register(r'processtypes', ProcessTypeViewSet, base_name='process_type')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
