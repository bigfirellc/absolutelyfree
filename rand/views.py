from django.http import HttpResponse
# Create your views here.
from .models import Bandname, Album
from django.template import loader
import random


def index(request):
    template = loader.get_template('rand/index.html')
    bandname_obj = getrandname()

    context = {
        'bandname_obj': bandname_obj,
    }
    return HttpResponse(template.render(context, request))


def getrandname():
    bandobjs = Bandname.objects.all()
    return random.choice(bandobjs)


def jumble(request):

    template = loader.get_template('rand/jumble.html')

    bandobjs = Bandname.objects.all()
    bandchoices = random.choices(bandobjs, k=2)
    bandjumble = ''

    for band in bandchoices:
        bandsplit = band.bandname_text.split(' ', 2)
        bandjumble += random.choice(bandsplit) + ' '

    context = {
        'bandjumble': bandjumble,
    }
    return HttpResponse(template.render(context, request))


def getrandalbum():
    albumobjs = Album.objects.all()
    return random.choice(albumobjs)


def albums(request):

    template = loader.get_template('rand/album.html')

    album_obj = getrandalbum()

    context = {
        'album_obj': album_obj,
    }
    return HttpResponse(template.render(context, request))
