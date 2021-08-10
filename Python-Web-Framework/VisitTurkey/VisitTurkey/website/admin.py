from django.contrib import admin

from VisitTurkey.website.models import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'user')
    search_fields = ['name']
    readonly_fields = ['user']


# admin.site.register(Place)
