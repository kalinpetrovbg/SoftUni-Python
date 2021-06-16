from django.urls import path
from todos_app.todos.views import index

urlpatterns = [
    path('', index)
]
