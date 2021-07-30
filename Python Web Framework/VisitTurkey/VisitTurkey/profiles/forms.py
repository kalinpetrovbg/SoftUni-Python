from django import forms
from VisitTurkey.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'is_complete')

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "Enter first name",
            }))

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "Enter last name",
            }))

    age = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "Enter your age",
            }))

    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "Enter your city",
            }))