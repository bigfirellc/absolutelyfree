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
    #full_bandname_list = Bandname.objects.order_by('-pub_date')
    template = loader.get_template('rand/index.html')

    bandcount = Bandname.objects.count()
    random_id = random.randint(1, bandcount)
    bandname_obj = Bandname.objects.get(id=random_id)

    context = {
        'bandname_obj': bandname_obj,
    }
    return HttpResponse(template.render(context, request))

def bandid(request, bandname_id):
    response = "Band name ID: %s"
    return HttpResponse(response % bandname_id)

def bandname(request, bandname_id):
    response = "You're looking at the name of band %s."
    return HttpResponse(response % bandname_id)
