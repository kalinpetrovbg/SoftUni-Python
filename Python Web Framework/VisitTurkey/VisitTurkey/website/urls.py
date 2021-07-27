from django.urls import path, include
from VisitTurkey.website.views import home_page, place_details, \
    create_place, all_places

urlpatterns = [
    path('', home_page, name='home page'),
    path('details/<int:pk>', place_details, name='place details'),
    path('create/', create_place, name='create place'),
    path('places/', all_places, name='all places'),
]