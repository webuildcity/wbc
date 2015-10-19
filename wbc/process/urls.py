# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register(r'processsteps', ProcessStepViewSet, base_name='processstep')
router.register(r'processtypes', ProcessTypeViewSet, base_name='processtype')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
