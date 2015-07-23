# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework import routers
from views import *

router = routers.DefaultRouter()
router.register(r'date', DateViewSet, base_name='date')
router.register(r'media', MediaViewSet, base_name='media')
router.register(r'Process_bplan', Process_bplanViewSet, base_name='Process_bplan')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
