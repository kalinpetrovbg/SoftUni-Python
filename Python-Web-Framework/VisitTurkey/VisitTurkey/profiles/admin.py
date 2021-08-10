from django.contrib import admin

from VisitTurkey.profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'age', 'city']
    search_fields = ['first_name', 'last_name']
    readonly_fields = ['first_name', 'last_name', 'user']


admin.site.register(Profile, ProfileAdmin)
