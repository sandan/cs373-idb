from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'stages/$', views.stages),
    url(r'stages/([0-9]{1,2})/$', views.stages),
    url(r'sponsors/$', views.sponsors),
    url(r'sponsors/([0-9]{1,2})/$', views.sponsors),
    url(r'artists/$', views.artists),
    url(r'artists/([0-9]{1,2})/$', views.artists),
    url(r'artists/([0-9]{1,2})/members/$', views.members),
    url(r'artists/([0-9]{1,2})/members/([0-9]{1,2})/$', views.members),
    url(r'artists/([0-9]{1,2})/photos/$', views.photos),
    url(r'artists/([0-9]{1,2})/photos/([0-9]{1,2})/$', views.photos),

    #url(r'([-a-zA-Z]+)/$', views.loadhtml),
)