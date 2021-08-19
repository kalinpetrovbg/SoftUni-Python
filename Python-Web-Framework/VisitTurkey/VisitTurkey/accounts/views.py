from django.contrib.auth import logout, get_user_model, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
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

    # sign in after a successful registration
    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


def log_out(request):
    logout(request)
    return redirect('home page')
