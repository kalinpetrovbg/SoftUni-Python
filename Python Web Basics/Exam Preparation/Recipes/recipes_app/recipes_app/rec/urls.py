from django.urls import path
from recipes_app.rec.views import home_page, create_recipe, \
    edit_recipe, delete_recipe, details, create_new, delete_item, edit_btn

urlpatterns = [
    path('', home_page, name='home'),
    path('create/', create_recipe, name='create'),
    path('edit/<int:pk>', edit_recipe, name='edit'),
    path('ed/<int:pk>', edit_btn, name='edit_btn'),
    path('delete/<int:pk>', delete_recipe, name='delete'),
    path('del/<int:pk>', delete_item, name='del'),
    path('details/<int:pk>', details, name='details'),
    path('cc/', create_new),
]