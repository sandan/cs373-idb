from django.shortcuts import render
from django.http import Http404

# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader

# from cs373.models import Sponsor

def index(request):
    c = Context()
    template = loader.get_template('index.html')
    return HttpResponse(template.render(c))

def stages(request,stage=0):
    stage = int(stage)
    if stage is 0:
        return render(request, 'stages.html')
    elif stage is 1:
        return render(request, 'honda-stage.html')
    elif stage is 2:
        return render(request, 'miller-lite-stage.html')
    elif stage is 3:
        return render(request, 'samsung-stage.html')
    else:
        raise Http404

def sponsors(request,sponsor=0):
    sponsor = int(sponsor)
    if sponsor is 0:
        return render(request, 'sponsors.html')
    elif sponsor is 1:
        return render(request, 'honda.html')
    elif sponsor is 2:
        return render(request, 'miller-lite.html')
    elif sponsor is 3:
        return render(request, 'samsung-galaxy.html')
    else:
        raise Http404


def artists(request,artist=0):
    artist = int(artist)
    if artist is 0:
        return render(request, 'artists.html')
    elif artist is 1:
        return render(request, 'eminem.html')
    elif artist is 2:
        return render(request, 'outkast.html')
    elif artist is 3:
        return render(request, 'pearljam.html')
    else:
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