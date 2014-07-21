from django.shortcuts import render
from django.http import Http404

# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader

from cs373.models import Artist, Stage, Sponsor

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
            return render(request, 'artist.html',{'artist':a})
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