from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


UserModel = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)


class SignInForm(forms.Form):
    user = None
    email = forms.EmailField(max_length=40)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput())

    def clean_password(self):
        self.user = authenticate(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Email and/or password is incorrect!')

    def save(self):
        return self.user
