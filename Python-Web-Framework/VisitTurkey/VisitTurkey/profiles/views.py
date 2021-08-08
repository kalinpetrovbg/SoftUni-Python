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