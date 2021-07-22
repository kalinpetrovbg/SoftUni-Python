from django.urls import path
from petstagram.pets.views import pet_details, pet_list, pet_landing_page, pet_like, only_cats, only_dogs

urlpatterns = [
    path('pet-list/', pet_list, name='list pets'),
    path('', pet_landing_page, name='landing page'),
    path('details/<int:pk>', pet_details, name='pet details'),
    path('like/<int:pk>', pet_like, name='pet_like'),
    path('list-cats/', only_cats, name='cats'),
    path('list-dogs/', only_dogs, name='dogs'),
]