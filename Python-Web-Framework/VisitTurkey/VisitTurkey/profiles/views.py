from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from VisitTurkey.profiles.forms import ProfileForm
from VisitTurkey.profiles.models import Profile


@login_required
def profile_info(request):
    profile = Profile.objects.get(pk=request.user.id)
    context = {
        'profile': profile
    }

    return render(request, 'accounts/profile.html', context)


# class ProfileDetailsView(DetailView):
#     template_name = 'accounts/profile.html'
#     model = Profile
#     context_object_name = 'profile'


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('profile info')

    # def get_success_url(self):
    #     profile_id = self.kwargs['pk']
    #     return reverse_lazy('profile info', kwargs={'pk': profile_id})


@login_required
def delete_profile(request):
    user = request.user

    if request.POST:
        user.delete()
        return redirect('home page')

    return render(request, 'accounts/delete_profile.html')
