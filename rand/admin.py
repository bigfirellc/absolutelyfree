from django.contrib import admin
from .models import Bandname


class BandnameAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    search_fields = ['bandname_text']
    list_display = ('bandname_text', 'pub_date')


admin.site.site_header = "Absolutely Free"
admin.site.site_title = "Absolutely Free"
admin.site.index_title = "Admin"
admin.site.register(Bandname, BandnameAdmin)
