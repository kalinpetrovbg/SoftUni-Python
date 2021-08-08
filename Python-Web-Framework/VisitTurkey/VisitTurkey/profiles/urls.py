from django.urls import path
from VisitTurkey.profiles.views import profile_info, edit_profile, delete_profile


urlpatterns = [
    path('', profile_info, name='profile info'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/', delete_profile, name='delete profile'),

    # Todo - maybe to add delete profile option ?!?
]


import VisitTurkey.profiles.signals