from django.conf.urls import patterns, url

from cs373 import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)