from django.urls import path

from VisitTurkey.website.views import index
from . import views

urlpatterns = [
    path('', index, name='home page'),
    path('details/<int:pk>', views.PlaceDetails.as_view(), name='place details'),
    path('create/', views.CreatePlace.as_view(), name='create place'),
    path('places/', views.AllPlaces.as_view(), name='all places'),
    path('delete/<int:pk>', views.DeletePlace.as_view(), name='delete place'),
    path('update/<int:pk>', views.UpdatePlace.as_view(), name='update place'),

]
