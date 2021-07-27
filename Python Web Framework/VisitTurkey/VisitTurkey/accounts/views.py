from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from VisitTurkey.accounts.forms import SignInForm


def log_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home page')
    else:
        form = SignInForm()

    context = {'form': form}

    return render(request, 'accounts/login.html', context)


def log_out(request):
    logout(request)
    return redirect('home page')


def register(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)
            return redirect('home page')
            # return redirect('log in')
    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'accounts/register.html', context)
