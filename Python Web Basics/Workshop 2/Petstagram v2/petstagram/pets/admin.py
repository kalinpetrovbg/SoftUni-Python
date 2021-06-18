from django.contrib import admin
from petstagram.pets.models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'age', 'likes_counter']

    def likes_counter(self, obj):
        return obj.like_set.count()

admin.site.register(Pet, PetAdmin)
