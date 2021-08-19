from django.urls import path

from VisitTurkey.accounts.views import log_out
from . import views

urlpatterns = [
    path('log-in/', views.LogInView.as_view(), name='log in'),
    path('log-out/', log_out, name='log out'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
