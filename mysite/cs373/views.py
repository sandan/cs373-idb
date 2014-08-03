import requests
from django.shortcuts import render
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.template import Context, loader
from cs373.models import *

### API imports
from cs373.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return render(request, 'index.html')

def groupapi1(request):
    """
    Get name of all stories in database. For each story get the name of the
    related characters. To access in template use
    for story,characters in data:
        <h2>{{story}}</h2>
        <ul>
        for character in characters:
            <li>{{character}}</li>
        </ul>
    """
    storiesUrl = 'http://domoench.pythonanywhere.com/api/stories/'
    charactersUrl = 'http://domoench.pythonanywhere.com/api/characters/'
    context = {'title':'List story and related characters'}
    stories = requests.get(storiesUrl).json()
    d = []
    for story in stories:
        characters  = []
        storyName = story['name']
        for cID in story['characters']:
            characterName = requests.get(charactersUrl+str(cID)+'/').json()['name']
            characters.append(characterName)
        z.append((storyName,characters))
    context['data'] = d
    return render(request, 'groupapi.html',context)

###########################
#                         #
#       Stage             #
#                         #
###########################
class StagesIndex(ListView):
    model=Stage
    context_object_name='stages'
    template_name='stages.html'

class StagePage(DetailView):
    model=Stage
    context_object_name='s'
    template_name='stage.html'

    def get_context_data(self, **kwargs):
        context = super(StagePage, self).get_context_data(**kwargs)
        try:
            s = super(StagePage,self).get_object()
            m = StageMedia.objects.get(st=s)

        except Stage.DoesNotExist or StageMedia.DoesNotExist:
            raise Http404

        context['m']=m
        return context

###########################
#                         #
#       Sponsor           #
#                         #
###########################

class SponsorsIndex(ListView):
    model=Sponsor
    context_object_name='sponsors'
    template_name='sponsors.html'

class SponsorPage(DetailView):
    model=Sponsor
    context_object_name='s'
    template_name='sponsor.html'

    def get_context_data(self, **kwargs):
        context = super(SponsorPage, self).get_context_data(**kwargs)
        try:
            s = super(SponsorPage,self).get_object()
            m = SponsorMedia.objects.get(sp=s)

        except Sponsor.DoesNotExist or SponsorMedia.DoesNotExist:
            raise Http404

        context['m']=m
        return context

###########################
#                         #
#       Artist            #
#                         #
###########################

class ArtistsIndex(ListView):
    model=Artist
    context_object_name='artists'
    template_name='artists.html'

class ArtistPage(DetailView):
    model=Artist
    context_object_name='a'
    template_name='artist.html'

    def get_context_data(self, **kwargs):
        context = super(ArtistPage, self).get_context_data(**kwargs)
        try:
            a = super(ArtistPage,self).get_object()
            m = ArtistMedia.objects.get(ar=a)

        except Artist.DoesNotExist or ArtistMedia.DoesNotExist:
            raise Http404

        context['m']=m
        return context


###########################
#                         #
#       API SECTION       #
#                         #
###########################


class StageList(APIView):




    def get(self, request):
        stages = Stage.objects.all()
        serializer = StageSerializer(stages, many=True)
        return Response(serializer.data, content_type="application/json")

    def post(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class StageDetail(APIView):


    def get(self, request, pk):
        try:
            stage = Stage.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StageSerializer(stage)
        return Response(serializer.data, content_type="application/json")

    def put(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class SponsorList(APIView):


    def get(self, request):
        sponsors = Sponsor.objects.all()
        serializer = SponsorSerializer(sponsors, many=True)
        return Response(serializer.data, content_type="application/json")

    def post(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class SponsorDetail(APIView):


    def get(self, request, pk):
        try:
            sponsor = Sponsor.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SponsorSerializer(sponsor)
        return Response(serializer.data, content_type="application/json")

    def put(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class ArtistList(APIView):


    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data, content_type="application/json")

    def post(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class ArtistDetail(APIView):


    def get(self, request, pk):
        try:
            artist = Artist.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ArtistSerializer(artist)
        return Response(serializer.data, content_type="application/json")

    def put(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)




class ArtistMediaDetail(APIView):

    def get(self, request, artist_id):
        try: 
            detail = ArtistMedia.objects.get(ar=Artist.objects.get(pk=artist_id))
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ArtistMediaSerializer(detail)

        return Response(serializer.data, content_type="application/json")

    def post(self, request, artist_id):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class StageMediaDetail(APIView):

    def get(self, request, stage_id):
        try: 
            detail = StageMedia.objects.get(st=Stage.objects.get(pk=stage_id))
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StageMediaSerializer(detail)

        return Response(serializer.data, content_type="application/json")

    def post(self, request, stage_id):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class SponsorMediaDetail(APIView):

    def get(self, request, sponsor_id):
        try: 
            detail = SponsorMedia.objects.get(sp=Sponsor.objects.get(pk=sponsor_id))
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SponsorMediaSerializer(detail)

        return Response(serializer.data, content_type="application/json")

    def post(self, request, sponsor_id):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
