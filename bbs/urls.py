from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'bbs.views.home'),
    url(r'^getOrt/$', 'bbs.views.getOrt'),
    # orte
    url(r'^orte/$', 'bbs.views.orte'),
    url(r'^orte/(?P<pk>\d+)/$', 'bbs.views.ort'),
    url(r'^orte/(?P<pk>\d+)/add/$', 'bbs.views.addPublicationToLocation', name='addPublicationToLocation'),
    # begriffe
    url(r'^begriffe/$', 'bbs.views.begriffe'),
    # modules
    url(r'^news/', include('news.urls')),
    url(r'^projekte/', include('projects.urls')),
    # url(r'^visualization/', include('visualization.urls')),
    # admin foo
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # user login
    url(r'^login/', 'bbs.views.login_user', name='User_login'),
    url(r'^logout/', 'bbs.views.logout_user', name='User_logout'),
    url(r'^new/', 'bbs.views.create_publication', name='New_publication'),

    # robots.txt and sitemap.xml
    (r'^robots\.txt$', TemplateView.as_view(template_name='bbs/robots.txt', content_type='text/plain')),
    (r'^sitemap\.xml$', TemplateView.as_view(template_name='bbs/sitemap.xml', content_type='text/plain')),
)
