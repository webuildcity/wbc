from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

from projects.views import OrteView,OrtView
from news import views

urlpatterns = patterns('',
    url(r'^$', 'bbs.views.home'),
    # orte
    url(r'^orte/$', OrteView.as_view()),
    url(r'^orte/(?P<pk>\d+)/$', OrtView.as_view()),
    # info
    url(r'^begriffe/$', 'bbs.views.begriffe'),
    # mails
    url(r'^news/abonnieren/$', 'news.views.abonnieren'),
    url(r'^news/validieren/(?P<code>.*)$', 'news.views.validieren'),
    url(r'^news/abbestellen/(?P<email>.*)$', 'news.views.abbestellen'),
    # admin foo
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # robots.txt
    (r'^robots\.txt$', TemplateView.as_view(template_name='bbs/robots.txt', content_type='text/plain')),
    (r'^sitemap\.xml$', TemplateView.as_view(template_name='bbs/sitemap.xml', content_type='text/plain')),
)
