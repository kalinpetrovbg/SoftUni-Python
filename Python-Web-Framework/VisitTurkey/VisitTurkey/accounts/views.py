from django.contrib.auth import logout, login
from django.shortcuts import render, redirect

from VisitTurkey.accounts.forms import SignInForm, SignUpForm


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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home page')
    else:
        form = SignUpForm()

    context = {'form': form}

    return render(request, 'accounts/register.html', context)
