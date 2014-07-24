from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView,DetailView

from django.template import Context, loader
from cs373.models import *

# API imports
#from cs373.serializers import *
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status

def index(request):
    return render(request, 'index.html')
"""
def stages(request,stage=0):
    stage = int(stage)
    if stage is 0:
        s = Stage.objects.all()
        return render(request, 'stages.html',{'stages':s})
    else:
        try:
            s = Stage.objects.get(pk=stage)
            return render(request, 'stage.html',{'stage':s})
        except Stage.DoesNotExist:
            raise Http404
"""
class StagesIndex(ListView):
    model=Stage
    contex_object_name='stages'
    template_name='stages.html'

class StagePage(DetailView):

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

class SponsorsIndex(ListView):
    model=Sponsor
    contex_object_name='sponsor'
    template_name='sponsors.html'

class SponsorPage(DetailView):

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

"""
DEPRECATED
def sponsors(request,sponsor=0):
    sponsor = int(sponsor)
    if sponsor is 0:
        s = Sponsor.objects.all()
        return render(request, 'sponsors.html',{'sponsors':s})
    else:
        try:
            s = Sponsor.objects.get(pk=sponsor)
            return render(request, 'sponsor.html',{'sponsor':s})
        except Sponsor.DoesNotExist:
            raise Http404

"""
class ArtistsIndex(ListView):
    model=Artist
    contex_object_name='artists'
    template_name='artists.html'

class ArtistPage(DetailView):
    template_name='artist.html'

    def get_context_data(self, **kwargs):
        context = super(ArtistPage, self).get_context_data(**kwargs)
        try:
            a = Artist.objects.get(pk=self.args[0])
            m = ArtistMedia.objects.get(ar=a)
            context['artist']=a
            context['media']=m

        except Artist.DoesNotExist or ArtistMedia.DoesNotExist:
            raise Http404
"""
DEPRECATED
def artists(request,artist=0):
    artist = int(artist)
    if artist is 0:
        a = Artist.objects.all()
        return render(request, 'artists.html',{'artists':a})
    else:
        try:
            a = Artist.objects.get(pk=artist)
            d = {'name':a.name,'label':a.label,'genre':a.genre,'origin':a.origin,'stage':a.stage}
            d['website'] = ''
            d['twitterwidget'] = ''
            d['youtubevideo'] = ''
            d['photo'] = ''
            return render(request, 'artist.html',d)
        except Artist.DoesNotExist:
            raise Http404
"""



###########################
#                         #
#       API SECTION       #
#                         #
###########################

"""
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
        return Response(serializer.data)

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
        return Response(serializer.data)

    def put(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class MemberList(APIView):



    def get(self, request, artist_id):
        try:
            members = Member.objects.filter(artist=artist_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data, content_type="application/json")

    def post(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class MemberDetail(APIView):


    def get(self, request, artist_id, pk):
        try:
            member = Member.objects.get(pk=pk, artist=artist_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def put(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class PhotoList(APIView):


    def get(self, request, artist_id):
        try:
            photo = Photo.objects.filter(artist=artist_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PhotoSerializer(members, many=True)
        return Response(serializer.data, content_type="application/json")

    def post(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class PhotoDetail(APIView):


    def get(self, request, artist_id, pk):
        try:
            photo = Photo.objects.get(pk=pk, artist=artist_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PhotoSerializer(photo)
        return Response(serializer.data)

    def put(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

"""