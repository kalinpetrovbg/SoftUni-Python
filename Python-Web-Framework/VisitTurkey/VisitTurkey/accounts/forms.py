from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class': "form-control",
                'placeholder': "Enter your email",
            }))

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password',
                   'class': "form-control",
                   'placeholder': "Create strong password",
                   }))

    password2 = forms.CharField(
        label="Repeat Password",
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password',
                   'class': "form-control",
                   'placeholder': "Repeat your password",
                   }))


class SignInForm(forms.Form):
    user = None
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class': "form-control",
                'placeholder': "Enter your email",
            }))
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password',
                   'class': "form-control",
                   'placeholder': "Enter your password",
                   }))

    def clean_password(self):
        self.user = authenticate(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Email and/or password is incorrect!')

    def save(self):
        return self.user
