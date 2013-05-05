from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from projekte.views import ProjekteView,VeroeffentlichungenView

urlpatterns = patterns('',
    url(r'^$', 'bbs.views.home'),
    # projects
    url(r'^projekte/$', ProjekteView.as_view()),
    url(r'^projekte/(?P<pk>\d+)/$', ProjekteView.as_view()),
    # bbp
    url(r'^veroeffentlichungen/$', VeroeffentlichungenView.as_view()),
    url(r'^veroeffentlichung/(?P<pk>\d+)/$', VeroeffentlichungenView.as_view()),
    # info
    url(r'^info/$', 'bbs.views.info'),
    # admin foo
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)), 
)
