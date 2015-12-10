from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'^neu/$', BlogEntryCreate.as_view(), name='blogentry_create'),
    url(r'^(?P<pk>[0-9]+)/bearbeiten/$', BlogEntryUpdate.as_view(), name='blogentry_update'),
    url(r'^(?P<pk>[0-9]+)/entfernen/$', BlogEntryDelete.as_view(), name='blogentry_delete'),
)