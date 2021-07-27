from django.urls import path, include

from VisitTurkey.accounts.views import log_in, log_out, register


urlpatterns = [
    path('log-in/', log_in, name='log in'),
    path('log-out/', log_out, name='log out'),
    path('register/', register, name='register'),
]