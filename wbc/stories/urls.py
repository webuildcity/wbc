# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework import routers
from views import *

router = routers.DefaultRouter()
router.register(r'stories', StoryViewSet, base_name='story')
router.register(r'list', StoryListViewSet, base_name='story_list')
router.register(r'basestep', BaseStepViewSet, base_name='basestep')
router.register(r'anchor', AnchorViewSet, base_name='anchor')
router.register(r'substep', SubstepViewSet, base_name='substep')

urlpatterns = patterns('',
    url(r'^', include(router.urls))
)