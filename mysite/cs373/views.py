# from django.shortcuts import render
from django.http import Http404
from django.views.generic.detail import DetailView
from cs373.models import *
from itertools import chain
from django.views.generic.dates import ArchiveIndexView
import requests
import random

### API imports
from cs373.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def page_not_found(request):
    return render(request, '404.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def groupapi(request):
    # characterUrl = 'http://domoench.pythonanywhere.com/api/characters/'
    # storiesUrl = 'http://domoench.pythonanywhere.com/api/stories/'
    # artifactUrl = 'http://domoench.pythonanywhere.com/api/artifacts/'

    # character = requests.get(characterUrl)
    # character = character.json()
    # character = random.choice(character)

    # stories = requests.get(storiesUrl)
    # stories = stories.json()
    # story_list = []
    # for story in stories:
    #     if character['id'] in story['characters']:
    #         story_list.append(story['name'])

    # artifacts = requests.get(artifactUrl)
    # artifacts = artifacts.json()
    # for artifact in artifacts:
    #     if character['id'] in artifact['owners']:
    #         artifact_list = artifact['name']

    # context = {'characterName':character['name']}
    # context['characterBio'] = character['description']
    # context['characterQuote'] = character['quote']
    # context['stories'] = story_list
    # context['artifacts'] = artifact_list

    context = {'characterName':'Harry Potter'}
    context['characterBio'] = "<p>Harry Potter is The Boy Who Lived, one of the most famous wizards of his time. In July 1980, Voldemort tried to murder Harry Potter while he was still a baby, afraid of a prophecy that said Potter would be the one to defeat him. His mother Lily Potter sacrificed herself for Harry, which gave Harry an ancient form of protection magic based on love. This protection caused Voldemort's killing curse to backfire onto himself, but left Harry with a lightning-shaped cursed scar on his forehead. This created a connection between Harry and Voldemort, allowing Harry to speak Parseltongue.</p>\r\n\r\n<p>Harry was raised by his aunt Petunia and uncle Vernon Dursley, who resented everything abnormal, including Harry. It wasn't until his 11th birthday that Potter discovered he was a wizard, and began attending Hogwarts School of Witchcraft and Wizardry with the inheritance his parents left behind. Here he met his dearest friends Ron Weasley and Hermione Granger. Harry became one of the youngest seekers for the Gryffindor Quidditch team during his first year. He also became one of the youngest Triwizard Tournament contestants during his fourth year.</p>\r\n\r\n<p>Along with other friends, Ron, Hermione, and Harry went on many adventures thrwarting evil throughout their school career. They stopped Professor Quirrell from bringing back Voldemort with the Philosopher's Stone. They stopped Tom Riddle's revival of the Chamber of Secrets. And finally in their last year at Hogwarts, they defeated Voldemort once and for all.</p>"
    context['characterQuote'] = "Every great wizard in history has started out as nothing more than what we are now, students. If they can do it, why not us?"

    return render(request,'groupapi.html',context)


###########################
#                         #
#       Stage             #
#                         #
###########################
class StagesIndex(ArchiveIndexView):

    def get_context_data(self, **kwargs):
        context = super(ArchiveIndexView, self).get_context_data(**kwargs)
        context['years']=sorted(set([s.get_yr() for s in stage_sponsor_yr.objects.order_by('-date')]), reverse=True)
        context['mediae']=StageMedia.objects.order_by('-year','stage__location')
        return context

class StagePage(DetailView):
    model=Stage
    context_object_name='s'
    template_name='stage.html'

    def get_context_data(self, **kwargs):
        context = super(StagePage, self).get_context_data(**kwargs)
        try:
            s = super(StagePage,self).get_object()
            m = StageMedia.objects.get(stage=s, year__year=self.kwargs['yr'])
            m.twitterwidget = m.twitter.split('/')[3]

        except Stage.DoesNotExist or StageMedia.DoesNotExist:
            raise Http404

        context['m']=m
        context['sponsors']={sp.sponsor for sp in stage_sponsor_yr.objects.filter(stage=s) if sp.date.year==int(self.kwargs['yr'])}
        context['artists']={a.artist for a in stage_artist_yr.objects.filter(stage=s) if a.date.year==int(self.kwargs['yr'])}
        return context

###########################
#                         #
#       Sponsor           #
#                         #
###########################

class SponsorsIndex(ArchiveIndexView):

    def get_context_data(self, **kwargs):
        context = super(ArchiveIndexView, self).get_context_data(**kwargs)
        context['years']=sorted(set([s.get_yr() for s in stage_sponsor_yr.objects.order_by('-date')]), reverse=True)
        context['sp']=stage_sponsor_yr.objects.order_by('-date','sponsor__name')
        return context


class SponsorPage(DetailView):
    model=Sponsor
    context_object_name='s'
    template_name='sponsor.html'

    def get_context_data(self, **kwargs):
        context = super(SponsorPage, self).get_context_data(**kwargs)
        try:
            s = super(SponsorPage,self).get_object()
            m = SponsorMedia.objects.get(sponsor=s)
            m.twitterwidget = m.twitter.split('/')[3]

        except Sponsor.DoesNotExist or SponsorMedia.DoesNotExist:
            raise Http404

        context['m']=m

        context['artists'] = set()
        for sponsor_stage in stage_sponsor_yr.objects.filter(sponsor=s):
            for sponsor_artist in stage_artist_yr.objects.filter(stage=sponsor_stage.stage, date__year=sponsor_stage.date.year):
                context['artists'].add(sponsor_artist.artist)

        context['stages']  = { media for r in stage_sponsor_yr.objects.filter(sponsor=s) for media in r.stage.stagemedia_set.filter(year__year=r.date.year) }

        return context

###########################
#                         #
#       Artist            #
#                         #
###########################

class ArtistsIndex(ArchiveIndexView):

    def get_context_data(self, **kwargs):
        context = super(ArchiveIndexView, self).get_context_data(**kwargs)
        context['years']=sorted(set([s.get_yr() for s in stage_artist_yr.objects.order_by('-date')]), reverse=True)
        context['ar']=stage_artist_yr.objects.order_by('-date','artist__name')
        return context

class ArtistPage(DetailView):
    model=Artist
    context_object_name='a'
    template_name='artist.html'

    def get_context_data(self, **kwargs):
        context = super(ArtistPage, self).get_context_data(**kwargs)
        try:
            a = super(ArtistPage,self).get_object()
            m = ArtistMedia.objects.get(artist=a)
            m.twitterwidget = m.twitter.split('/')[3]

        except Artist.DoesNotExist or ArtistMedia.DoesNotExist:
            raise Http404

        context['m']=m
        context['stages']={ media for r in stage_artist_yr.objects.filter(artist=a) for media in r.stage.stagemedia_set.filter(year__year=r.date.year) }

        context['sponsors']= set()
        for stage_artists in stage_artist_yr.objects.filter(artist=a):
            for stage_sponsor in stage_sponsor_yr.objects.filter(stage=stage_artists.stage, date__year=stage_artists.date.year):
                context['sponsors'].add(stage_sponsor.sponsor)

        return context


###########################
#                         #
#       API SECTION       #
#                         #
###########################

###########################
#                         #
#       STAGES            #
#                         #
###########################

class StageList(APIView):

    def get(self, request):
        stages = Stage.objects.all()
        result=[]
        for s in stages:
            years=chain(stage_artist_yr.objects.filter(stage__location=s.location),stage_sponsor_yr.objects.filter(stage__location=s.location))
            result+=[ dict( [ ('location', s.location), ('years',list({ y.get_yr() for y in years}))])]
        return Response(result, content_type="application/json")

    def post(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class StageDetail(APIView):

    def get(self, request, pk):
        try:
            stage = Stage.objects.get(location=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        years=stage_artist_yr.objects.filter(stage__location=pk)
        result = StageSerializer(stage).data
        result['years']=list({ x.get_yr() for x in years})
        return Response(result, content_type="application/json")

    def put(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class StageDetailYear(APIView):

    def get(self, request, pk,yr):
        try:
            stage = Stage.objects.get(location=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        sponsor=stage_sponsor_yr.objects.filter(date__year=yr, stage__location=pk)
        artistas=stage_artist_yr.objects.filter(stage__location=pk, date__year=yr)
        result= StageSerializer(stage).data
        result['artists']=list({ x.id for x in artistas})
        try:
            result['sponsor']=sponsor[0]
        except Exception:
            result['sponsor']=''

        result['year']=yr
        return Response(result, content_type="application/json")

    def put(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


###########################
#                         #
#       SPONSORS          #
#                         #
###########################

class SponsorList(APIView):

    def get(self, request):
        result = SponsorSerializer(Sponsor.objects.all(),many=True).data
        for e in result:
            try:
                e['years']=[]
                e['stage_locations']=[]
                for s in stage_sponsor_yr.objects.filter(sponsor__id=e['id']):
                    e['years']+=[s.get_yr()]
                    e['stage_locations']+=[s.stage.location]
                e['stage_locations']=list(set(e['stage_locations']))
            except Exception:
                e['years']=[]
                e['stage_locations']=[]

        return Response(result, content_type="application/json")

    def post(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class SponsorDetail(APIView):

    def get(self, request, pk):
        try:
            sponsor = Sponsor.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        result = SponsorSerializer(sponsor).data
        result['years']=[]
        result['stage_locations']=[]
        for s in stage_sponsor_yr.objects.filter(sponsor__id=pk):
            result['years']+=[ s.get_yr()]
            result['stage_locations']+=[s.stage.location]
        result['stage_locations']=list(set(result['stage_locations']))
        return Response(result, content_type="application/json")

    def put(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class SponsorDetailYear(APIView):

    def get(self, request,yr):
        try:
            result=SponsorSerializer(Sponsor.objects.all(), many=True).data
            for e in result:
                stage_rel=stage_sponsor_yr.objects.filter(date__year=yr, sponsor__id=e['id'])[0]
                e['stage_location']=stage_rel.stage.location
        except:
            e['stage_location']=''
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(result, content_type="application/json")

    def put(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


###########################
#                         #
#       ARTISTS           #
#                         #
###########################

class ArtistList(APIView):


    def get(self, request):
        result = ArtistSerializer(Artist.objects.all(),many=True).data
        for e in result:
            try:
                e['years']=[]
                e['stage_locations']=[]
                for s in stage_artist_yr.objects.filter(artist__id=e['id']):
                    e['years']+=[s.get_yr()]
                    e['stage_locations']+=[s.stage.location]
                e['stage_locations']=list(set(e['stage_locations']))
            except Exception:
                e['years']=[]
                e['stage_locations']=[]

        return Response(result, content_type="application/json")

    def post(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class ArtistDetail(APIView):

    def get(self, request, pk):
        try:
            artist = Artist.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        result = ArtistSerializer(artist).data
        result['years']=[]
        result['stage_locations']=[]
        for s in stage_artist_yr.objects.filter(artist__id=pk):
            result['years']+=[ s.get_yr()]
            result['stage_locations']+=[s.stage.location]
        result['stage_locations']=list(set(result['stage_locations']))
        return Response(result, content_type="application/json")

    def put(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class ArtistDetailYear(APIView):

    def get(self, request,yr):
        try:
            result=ArtistSerializer(Artist.objects.all(), many=True).data
            for e in result:
                stage_rel=stage_artist_yr.objects.filter(date__year=yr, artist__id=e['id'])[0]
                e['stage_location']=stage_rel.stage.location
        except:
            e['stage_location']=''
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(result, content_type="application/json")

    def put(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, artist_id, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



###########################
#                         #
#       MEDIA             #
#                         #
###########################

class ArtistMediaDetail(APIView):

    def get(self, request, artist_id):
        try:
            detail = ArtistMedia.objects.get(artist=Artist.objects.get(id=artist_id))
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ArtistMediaSerializer(detail)

        return Response(serializer.data, content_type="application/json")

    def post(self, request, artist_id):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class StageMediaDetail(APIView):

    def get(self, request, loc, yr):
        try:
            detail = StageMedia.objects.get(stage=Stage.objects.get(location=loc), year__year=yr)#TODO
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StageMediaSerializer(detail).data
        serializer['location']=detail.stage.location
        serializer['year']=detail.year.year

        return Response(serializer, content_type="application/json")

    def post(self, request, loc, yr):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class StageMediaList(APIView):

    def get(self, request, loc):
        try:
            s=Stage.objects.get(location=loc)
            media = StageMedia.objects.filter(stage=s)
            result = []
            for e in media:
                ser=StageMediaSerializer(e).data
                ser['location']=s.location
                ser['year']=e.year.year
                result+=[ser]

        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(result, content_type="application/json")

    def post(self, request, loc):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class SponsorMediaDetail(APIView):

    def get(self, request, sponsor_id):
        try:
            detail = SponsorMedia.objects.get(sponsor=Sponsor.objects.get(id=sponsor_id))
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SponsorMediaSerializer(detail)

        return Response(serializer.data, content_type="application/json")

    def post(self, request, sponsor_id):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
from django.shortcuts import render

# Create your views here.
