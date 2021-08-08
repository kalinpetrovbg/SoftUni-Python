from django.urls import path
from VisitTurkey.profiles.views import profile_info


urlpatterns = [
    path('', profile_info, name='profile info')

]


import VisitTurkey.profiles.signals