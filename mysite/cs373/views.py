from django.shortcuts import render
from django.http import Http404

# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader

from cs373.models import Artist, Stage, Sponsor, Photo, Member

# API imports
from cs373.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return render(request, 'index.html')

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

def members(request,artist,member=0):
    member = int(member)
    if member is 0:
        return render(request, 'members.html')
    elif member is 1:
        return render(request, 'member0.html')
    elif member is 2:
        return render(request, 'member2.html')
    elif member is 3:
        return render(request, 'member3.html')
    else:
        raise Http404

def photos(request,artist,photo=0):
    photo = int(photo)
    if photo is 0:
        return render(request, 'photos.html')
    elif photo is 1:
        return render(request, 'photo0.html')
    elif photo is 2:
        return render(request, 'photo2.html')
    elif photo is 3:
        return render(request, 'photo3.html')
    else:
        raise Http404


###########################
#                         #
#       API SECTION       #
#                         #
###########################

class StageList(APIView):
    """ 
    List all stages
    """

    def get(self, request):
        stages = Stage.objects.all()
        serializer = StageSerializer(stages, many=True)
        return Response(serializer.data, content_type="application/json")

    def post(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class StageDetail(APIView):
    """
    Get a single stage
    """

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
    """ 
    List all sponsors
    """

    def get(self, request):
        sponsors = Sponsor.objects.all()
        serializer = SponsorSerializer(sponsors, many=True)
        return Response(serializer.data, content_type="application/json")

    def post(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class SponsorDetail(APIView):
    """
    Get a single sponsor
    """

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
    """ 
    List all artists
    """

    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data, content_type="application/json")

    def post(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)        

class ArtistDetail(APIView):
    """
    Get a single artist
    """

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
    """ 
    List all for a specific artist
    """

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
    """
    Get a single artist
    """

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
    """ 
    List all for a specific artist
    """

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
    """
    Get a single artist
    """

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

