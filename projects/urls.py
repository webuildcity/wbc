from django.conf.urls import patterns, include, url

from projects import views

urlpatterns = patterns('projects.urls',
    url(r'^orte/$', views.orte),
    url(r'^orte/(?P<pk>\d+)/$', views.ort),
    url(r'^veroeffentlichungen/$', views.veroeffentlichungen),
    url(r'^veroeffentlichungen/(?P<pk>\d+)/$', views.veroeffentlichung),
    url(r'^verfahrensschritte/$', views.verfahrensschritte),
    url(r'^verfahrensschritte/(?P<pk>\d+)/$', views.verfahrensschritt)
)
