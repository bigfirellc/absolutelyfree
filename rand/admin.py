from django.contrib import admin
from .models import Album, Bandname


class AlbumAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    search_fields = ['name']
    list_display = ('name', 'pub_date')


class BandnameAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    search_fields = ['bandname_text']
    list_display = ('bandname_text', 'pub_date')


admin.site.site_header = "Absolutely Free"
admin.site.site_title = "Absolutely Free"
admin.site.index_title = "Admin"
admin.site.register(Album, AlbumAdmin)
admin.site.register(Bandname, BandnameAdmin)
