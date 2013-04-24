from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from projects.views import ProjectsView,BBPView

urlpatterns = patterns('',
    url(r'^$', 'bbs.views.home'),
    # projects
    url(r'^projects/$', ProjectsView.as_view()),
    url(r'^projects/(?P<pk>\d+)/$', ProjectsView.as_view()),
    # bbp
    url(r'^bbp/$', BBPView.as_view()),
    url(r'^bbp/(?P<pk>\d+)/$', BBPView.as_view()),
    #typen
    url(r'^glossar/$', 'bbs.views.glossar'),
    # admin foo
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)), 
)
