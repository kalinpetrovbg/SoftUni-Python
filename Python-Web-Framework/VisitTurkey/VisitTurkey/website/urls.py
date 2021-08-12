from django.urls import path, include
from . import views
from VisitTurkey.website.views import place_details, create_place, index

urlpatterns = [
    path('', index, name='home page'),
    path('details/<int:pk>', place_details, name='place details'),
    path('create/', create_place, name='create place'),
    path('places/', views.AllPlaces.as_view(), name='all places'),
    path('delete/<int:pk>', views.DeletePlace.as_view(), name='delete place'),
    path('update/<int:pk>', views.UpdatePlace.as_view(), name='update place'),

]