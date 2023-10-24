from django.contrib import admin
from .models import Album, Bandname, AlbumResource, BandnameResource
from import_export.admin import ImportExportModelAdmin
from django.utils.translation import gettext_lazy as _


class AlbumAdmin(ImportExportModelAdmin):        
    resource_classes = [AlbumResource]
    date_hierarchy = 'pub_date'
    search_fields = ['name']
    list_display = ('name', 'pub_date')


class BandnameAdmin(ImportExportModelAdmin):
    resource_classes = [BandnameResource]
    date_hierarchy = 'pub_date'
    search_fields = ['bandname_text']
    list_display = ('bandname_text', 'pub_date')
    


admin.site.site_header = "Absolutely Free"
admin.site.site_title = "Absolutely Free"
admin.site.index_title = "Admin"
admin.site.register(Album, AlbumAdmin)
admin.site.register(Bandname, BandnameAdmin)
