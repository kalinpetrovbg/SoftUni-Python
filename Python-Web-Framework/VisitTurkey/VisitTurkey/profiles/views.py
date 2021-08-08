from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from VisitTurkey.profiles.forms import ProfileForm
from VisitTurkey.profiles.models import Profile


@login_required
def profile_info(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile info')
    else:
        form = ProfileForm(instance=profile)

    context = {'form': form}

    return render(request, 'accounts/profile.html', context)


@login_required
def edit_profile(request):
    user_id = request.user.id
    profile = Profile.objects.get(pk=user_id)
    if request.method == 'GET':
        form = ProfileForm(instance=profile)
        context = {'form': form, 'profile': profile}

        return render(request, 'accounts/edit_profile.html', context)

    else:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile info')

        context = {'form': form, 'profile': profile}

        return render(request, 'accounts/edit_profile.html', context)


@login_required
def delete_profile(request):
    user = request.user

    if request.POST:
        user.delete()
        return redirect('home page')

    return render(request, 'accounts/delete_profile.html')
