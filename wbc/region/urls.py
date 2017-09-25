# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'muncipalities', MuncipalityViewSet, base_name='muncipality')
router.register(r'districts', DistrictViewSet, base_name='district')
router.register(r'quarters', QuarterViewSet, base_name='quarter')
router.register(r'departments', DepartmentViewSet, base_name='department')

urlpatterns = [
    url(r'', include(router.urls)),
]
