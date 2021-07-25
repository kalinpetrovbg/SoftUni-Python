from django.contrib import admin
from VisitTurkey.website.models import Place

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type', 'description')
    # list_filter = ('type',)

admin.site.register(Place)


