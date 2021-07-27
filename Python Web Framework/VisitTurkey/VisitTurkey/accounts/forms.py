from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class SignInForm(forms.Form):
    user = None
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput())

    def clean_password(self):
        self.user = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Username and/or password is incorrect!')

    def save(self):
        return self.user
