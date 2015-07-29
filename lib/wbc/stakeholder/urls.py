# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework import routers
from views import *

router = routers.DefaultRouter()
router.register(r'stakeholders', StakeholderViewSet, base_name='stakeholder')
router.register(r'stakeholderRoles', StakeholderRoleViewSet, base_name='stakeholder_role')
router.register(r'departments', DepartmentViewSet, base_name='department')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
