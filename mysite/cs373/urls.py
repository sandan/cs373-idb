from django.conf.urls import patterns, url

from cs373.views import ArtistPage, ArtistsIndex, SponsorsIndex, SponsorPage, StagesIndex, StagePage, index

"""
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
"""
urlpatterns = patterns('',


    url(r'^$', index, name='index'),

    url(r'stages/$', StagesIndex.as_view()),
    url(r'stages/(?P<pk>\d+)/$', StagePage.as_view()),

    url(r'sponsors/$', SponsorsIndex.as_view()),
    url(r'sponsors/(?P<pk>\d+)/$', SponsorPage.as_view()),

    url(r'artists/$', ArtistsIndex.as_view()),
    url(r'artists/(?P<pk>\d+)/$', ArtistPage.as_view()),

    #DEPRECATED
    #url(r'artists/([0-9]{1,2})/members/$', views.members),
    #url(r'artists/([0-9]{1,2})/members/([0-9]{1,2})/$', views.members),
    #url(r'artists/([0-9]{1,2})/photos/$', views.photos),
    #url(r'artists/([0-9]{1,2})/photos/([0-9]{1,2})/$', views.photos),

    #url(r'([-a-zA-Z]+)/$', views.loadhtml),
)