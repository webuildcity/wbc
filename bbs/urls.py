from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from projekte.views import ProjekteView,VeroeffentlichungenView
from news import views

urlpatterns = patterns('',
    url(r'^$', 'bbs.views.home'),
    # projects
    url(r'^orte/$', ProjekteView.as_view()),
    url(r'^orte/(?P<pk>\d+)/$', ProjekteView.as_view()),
    # bbp
    url(r'^veroeffentlichungen/$', VeroeffentlichungenView.as_view()),
    url(r'^veroeffentlichungen/(?P<pk>\d+)/$', VeroeffentlichungenView.as_view()),
    # info
    url(r'^info/$', 'bbs.views.info'),
    # mails
    url(r'^news/abonieren/$', 'news.views.abonieren'),
    url(r'^news/validieren/(?P<code>.*)$', 'news.views.validieren'),
    url(r'^news/abbestellen/(?P<email>.*)$', 'news.views.abbestellen'),
    # admin foo
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls))
)
