from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'api/stages/$', views.StageList.as_view()),
    url(r'api/stages/(?P<pk>[0-9]+)/$', views.StageDetail.as_view()),
    url(r'api/sponsors/$', views.SponsorList.as_view()),
    url(r'api/sponsors/(?P<pk>[0-9]+)/$', views.SponsorDetail.as_view()),
    url(r'api/artists/$', views.ArtistList.as_view()),
    url(r'api/artists/(?P<pk>[0-9]+)/$', views.ArtistDetail.as_view()),
    url(r'api/artists/(?P<artist_id>[0-9]+)/members/$', views.MemberList.as_view()),
    url(r'api/artists/(?P<artist_id>[0-9]+)/members/(?P<pk>[0-9]+)/$', views.MemberDetail.as_view()),
    url(r'api/artists/(?P<artist_id>[0-9]+)/photos/$', views.MemberList.as_view()),
    url(r'api/artists/(?P<artist_id>[0-9]+)/photos/(?P<pk>[0-9]+)/$', views.PhotoDetail.as_view()),
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