# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework import routers
from views import *

router = routers.DefaultRouter()
router.register(r'organizations', OrganizationViewSet, base_name='organization')
router.register(r'persons', PersonViewSet, base_name='person')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
