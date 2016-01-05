from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'^neu/$', BlogEntryCreate.as_view(), name='blogentry_create'),
    url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/bearbeiten/$', BlogEntryUpdate.as_view(), name='blogentry_update'),
    url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/entfernen/$', BlogEntryDelete.as_view(), name='blogentry_delete'),
)