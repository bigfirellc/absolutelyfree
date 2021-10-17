from django.http import HttpResponse
from datetime import datetime
from .models import Album, Bandname
from django.template import loader
import random
from django.views.generic import ListView, TemplateView
from django.db.models import Q

def index(request):
    template = loader.get_template('rand/index.html')
    bandname_obj = getrandname()

    context = {
        'bandname_obj': bandname_obj,
    }
    return HttpResponse(template.render(context, request))


def getrandname():
    bandobjs = Bandname.objects.all()
    random.seed(datetime.now())
    return random.choice(bandobjs)


def jumble(request):

    template = loader.get_template('rand/jumble.html')

    bandobjs = Bandname.objects.all()
    random.seed(datetime.now())
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
    random.seed(datetime.now())
    return random.choice(albumobjs)


def albums(request):

    template = loader.get_template('rand/album.html')

    album_obj = getrandalbum()

    context = {
        'album_obj': album_obj,
    }
    return HttpResponse(template.render(context, request))

class SearchPageView(TemplateView):
    template_name = 'search.html'

class SearchResultsView(ListView):
    model = Bandname
    template_name = 'rand/search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Bandname.objects.filter(
            Q(bandname_text__icontains=query)
        )
        return object_list