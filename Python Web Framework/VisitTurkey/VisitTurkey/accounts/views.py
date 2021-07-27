from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def log_in(request):
    user = authenticate(username='kalin', password='kalin123')
    login(request, user)
    return redirect('home page')


def log_out(request):
    logout(request)
    return redirect('home page')


def register(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')  # OR TO SIGN IN
    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'accounts/register.html', context)
