from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader
import random

def index(request):
    #full_bandname_list = Bandname.objects.order_by('-pub_date')
    template = loader.get_template('well-known/index.html')
    return HttpResponse(template.render(context, request))