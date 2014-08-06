from django.conf.urls import patterns, url
from cs373.views import *
from django.views.generic.dates import ArchiveIndexView

urlpatterns = patterns('',
    url(r'api/stages/$', StageList.as_view()),
    url(r'api/stages/(?P<pk>[0-9]+)/$', StageDetail.as_view()),
    url(r'api/stages/(?P<pk>[0-9]+)/(?P<yr>[0-9]+)/$', StageDetailYear.as_view()),

    url(r'api/sponsors/$', SponsorList.as_view()),
    url(r'api/sponsors/(?P<pk>[0-9]+)/$', SponsorDetail.as_view()),
    url(r'api/sponsors/year/(?P<yr>[0-9]+)/$', SponsorDetailYear.as_view()),

    url(r'api/artists/$', ArtistList.as_view()),
    url(r'api/artists/(?P<pk>[0-9]+)/$', ArtistDetail.as_view()),
    url(r'api/artists/year/(?P<yr>[0-9]+)/$', ArtistDetailYear.as_view()),

    url(r'api/stages/(?P<loc>[0-9]+)/media/(?P<yr>[0-9]+)/$', StageMediaDetail.as_view()),
    url(r'api/stages/(?P<loc>[0-9]+)/media/$', StageMediaList.as_view()),

    url(r'api/sponsors/(?P<sponsor_id>[0-9]+)/media/$', SponsorMediaDetail.as_view()),
    url(r'api/artists/(?P<artist_id>[0-9]+)/media/$', ArtistMediaDetail.as_view()),

    url(r'^$', index, name='index'),

    url(r'stages/$', StagesIndex.as_view(model=StageMedia, date_field='year', template_name='stages.html', context_object_name='medias', allow_future=True)),
    url(r'stages/(?P<pk>\d+)/(?P<yr>[-\w]+)/$', StagePage.as_view(), name='stage_detail'),

    url(r'sponsors/$', SponsorsIndex.as_view(model=stage_sponsor_yr, date_field='date', template_name='sponsors.html', context_object_name='relations', allow_future=True)),
    url(r'sponsors/(?P<pk>\d+)/$', SponsorPage.as_view(), name='sponsor_detail'),


    url(r'artists/$', ArtistsIndex.as_view(model=stage_artist_yr, date_field='date', template_name='artists.html', context_object_name='relations', allow_future=True)),
    url(r'artists/(?P<pk>\d+)/$', ArtistPage.as_view(), name='artist_detail'),

)
