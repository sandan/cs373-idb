from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'sponsors/([-a-zA-Z]+)/', views.sponsor),
    url(r'([-a-zA-Z]+)/$', views.loadhtml),
)