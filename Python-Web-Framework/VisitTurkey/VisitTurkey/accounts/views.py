from django.contrib.auth import logout, get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView

from VisitTurkey.accounts.forms import SignInForm, SignUpForm

UserModel = get_user_model()


class LogInView(LoginView):
    template_name = 'accounts/login.html'
    form_class = SignInForm

    def get_success_url(self):
        return reverse('home page')


class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    model = UserModel
    form_class = SignUpForm
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LogOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('home page')
