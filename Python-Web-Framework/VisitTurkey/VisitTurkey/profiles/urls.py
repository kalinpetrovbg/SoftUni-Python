from django.urls import path
from VisitTurkey.profiles.views import delete_profile, profile_info
from . import views

urlpatterns = [
    path('info/', profile_info, name='profile info'),
    path('edit/<int:pk>', views.ProfileEditView.as_view(), name='edit profile'),
    path('delete/', delete_profile, name='delete profile'),
]


import VisitTurkey.profiles.signals