# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from wbc.news import views

urlpatterns = patterns('news.urls',
    url(r'^abonnieren/$', views.abonnieren),
    url(r'^validieren/(?P<code>.*)$', views.validieren),
    url(r'^abbestellen/(?P<email>.*)$', views.abbestellen),
)
