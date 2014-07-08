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

def loadhtml(request,f):
    c = Context()
    f += '.html'
    template = loader.get_template(f)
    return HttpResponse(template.render(c))

def sponsor(request,f):
    f = f.title().replace('-', ' ')
    try:
        s = Sponsor.objects.get(name=f)
    except Sponsor.DoesNotExist:
        raise Http404
    return render(request, 'sponsor.html', {'sponsor': s})


# def honda(request):
#     c = Context()
#     template = loader.get_template('honda.html')
#     return HttpResponse(template.render(c))

# def millerlite(request):
#     c = Context()
#     template = loader.get_template('miller-lite.html')
#     return HttpResponse(template.render(c))

# def sponsors(request):
#     c = Context()
#     template = loader.get_template('sponsors.html')
#     return HttpResponse(template.render(c))