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
    template_name='stage.html'

    def get_context_data(self, **kwargs):
        context = super(StagePage, self).get_context_data(**kwargs)
        try:
            s = Stage.objects.get(pk=self.args[0])
            m = StageMedia.objects.get(st=s)
            context['stage']=s
            context['media']=m
        except Stage.DoesNotExist or StageMedia.DoesNotExist:
            raise Http404

###########################
#                         #
#       Sponsor           #
#                         #
###########################

class SponsorsIndex(ListView):
    model=Sponsor
    context_object_name='sponsor'
    template_name='sponsors.html'

class SponsorPage(DetailView):
    model=Sponsor
    template_name='sponsor.html'

    def get_context_data(self, **kwargs):
        context = super(SponsorPage, self).get_context_data(**kwargs)
        try:
            sp = Sponsor.objects.get(pk=self.args[0])
            m = SponsorMedia.objects.get()
            context['sponsor']=sp
            context['media']=m
        except Sponsor.DoesNotExist or SponsorMedia.DoesNotExist:
            raise Http404

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
    template_name='artist.html'
    model=Artist

    def get_context_data(self, **kwargs):
        context = super(ArtistPage, self).get_context_data(**kwargs)
        try:
            a = Artist.objects.get(pk=self.kwargs['pk'])
            m = ArtistMedia.objects.get(ar=a)
            context['a']=a
            context['m']=m
            return context

        except Artist.DoesNotExist or ArtistMedia.DoesNotExist:
            raise Http404


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

class StageMediaDetail(APIView):

    def get(self, request, stage_id):
        try: 
            detail = StageMedia.objects.get(st=Stage.objects.get(pk=stage_id))
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StageMediaSerializer(detail)

        return Response(serializer.data, content_type="application/json")

class SponsorMediaDetail(APIView):

    def get(self, request, sponsor_id):
        try: 
            detail = SponsorMedia.objects.get(sp=Sponsor.objects.get(pk=sponsor_id))
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SponsorMediaSerializer(detail)

        return Response(serializer.data, content_type="application/json")
