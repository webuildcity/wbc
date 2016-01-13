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
    url(r'^neu/$', StakeholderCreate.as_view(), name='stakeholder_create'),
    url(r'^(?P<pk>[0-9]+)/bearbeiten/$', StakeholderUpdate.as_view(), name='stakeholder_update'),
    url(r'^(?P<pk>[0-9]+)/entfernen/$', StakeholderDelete.as_view(), name='stakeholder_delete'),
    url(r'^(?P<pk>[0-9]+)/photo_upload/', 'wbc.stakeholder.views.photo_upload', name="stakeholder_photo_upload"),

)
