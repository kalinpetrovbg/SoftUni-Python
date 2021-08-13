from django import forms

from VisitTurkey.website.models import Place


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        exclude = {'user'}

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "Name of the place",
            }))

    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "Enter accurate location",
            }))

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': "form-control",
                'placeholder': "Enter nice and clear description",
                'rows': "3",
            }))

