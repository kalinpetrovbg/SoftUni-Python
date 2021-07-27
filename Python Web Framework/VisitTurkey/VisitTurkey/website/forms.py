from django import forms
from VisitTurkey.website.models import Place
from django.conf import settings
from os.path import join
import os


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'
