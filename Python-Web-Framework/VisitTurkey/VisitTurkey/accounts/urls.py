from django.urls import path

from . import views

urlpatterns = [
    path('log-in/', views.LogInView.as_view(), name='log in'),
    path('log-out/', views.LogOutView.as_view(), name='log out'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
