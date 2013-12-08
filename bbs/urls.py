from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from projekte.views import ProjekteView,ProjektView
from news import views

urlpatterns = patterns('',
    url(r'^$', 'bbs.views.home'),
    # orte
    url(r'^orte/$', ProjekteView.as_view()),
    url(r'^orte/(?P<pk>\d+)/$', ProjektView.as_view()),
    # info
    url(r'^begriffe/$', 'bbs.views.begriffe'),
    # mails
    url(r'^news/abonnieren/$', 'news.views.abonnieren'),
    url(r'^news/validieren/(?P<code>.*)$', 'news.views.validieren'),
    url(r'^news/abbestellen/(?P<email>.*)$', 'news.views.abbestellen'),
    # admin foo
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls))
)
