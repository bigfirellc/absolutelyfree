from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Bandname
from django.template import loader
import random

#def index(request):
 #   latest_bandname_list = Bandname.objects.order_by('-pub_date')[:5]
 #   count = str(Bandname.objects.count())
 #   output =  "The latest 5 band names in the database are: <ul><li>"
 #   output += '<li>'.join([b.bandname_text for b in latest_bandname_list])
 #   output += ".</ul>There is a total of %s entries in the database." % count
 #   return HttpResponse(output)

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


def bandid(request, bandname_id):
    response = "Band name ID: %s"
    return HttpResponse(response % bandname_id)

def bandname(request, bandname_id):
    response = "You're looking at the name of band %s."
    return HttpResponse(response % bandname_id)
