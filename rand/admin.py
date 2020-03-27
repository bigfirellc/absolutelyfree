from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Bandname, Album

admin.site.register(Bandname)
admin.site.register(Album)