from django.contrib import admin
from recipes_app.rec.models import Recipe


@admin.register(Recipe)
class AdminFields(admin.ModelAdmin):
    list_display = ['title', 'ingredients', 'time']
