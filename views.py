from django.shortcuts import render
from django.http import Http404

# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader

from cs373.models import Sponsor

def index(request):
    c = Context()
    template = loader.get_template('index.html')
    return HttpResponse(template.render(c))

def stages(request,stage=-1):
    stage = int(stage)
    if stage is -1:
        return render(request, 'stages.html')
    elif stage is 0:
        return render(request, 'stages0.html')
    elif stage is 2:
        return render(request, 'stages2.html')
    elif stage is 3:
        return render(request, 'stages3.html')
    else:
        raise Http404

def sponsors(request,sponsor=-1):
    sponsor = int(sponsor)
    if sponsor is -1:
        return render(request, 'sponsors.html')
    elif sponsor is 0:
        return render(request, 'sponsor0.html')
    elif sponsor is 2:
        return render(request, 'sponsor2.html')
    elif sponsor is 3:
        return render(request, 'sponsor3.html')
    else:
        raise Http404


def artists(request,artist=-1):
    artist = int(artist)
    if artist is -1:
        return render(request, 'artists.html')
    elif artist is 0:
        return render(request, 'artist0.html')
    elif artist is 2:
        return render(request, 'artist2.html')
    elif artist is 3:
        return render(request, 'artist3.html')
    else:
        raise Http404

def members(request,artist,member=-1):
    member = int(member)
    if member is -1:
        return render(request, 'members.html')
    elif member is 0:
        return render(request, 'member0.html')
    elif member is 2:
        return render(request, 'member2.html')
    elif member is 3:
        return render(request, 'member3.html')
    else:
        raise Http404

def photos(request,artist,photo=-1):
    photo = int(photo)
    if photo is -1:
        return render(request, 'photos.html')
    elif photo is 0:
        return render(request, 'photo0.html')
    elif photo is 2:
        return render(request, 'photo2.html')
    elif photo is 3:
        return render(request, 'photo3.html')
    else:
        raise Http404

# def loadhtml(request,f):
#     c = Context()
#     f += '.html'
#     template = loader.get_template(f)
#     return HttpResponse(template.render(c))

# def sponsor(request,f):
#     f = f.title().replace('-', ' ')
#     try:
#         s = Sponsor.objects.get(name=f)
#     except Sponsor.DoesNotExist:
#         raise Http404
#     return render(request, 'sponsor.html', {'sponsor': s})