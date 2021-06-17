from django.urls import path
from todos_app.todos.views import index, create_todo, delete_todo, change_todo

urlpatterns = [
    path('', index),
    path('todos-add', create_todo),
    path('todos-del', delete_todo),
    path('todo-change/<int:pk>', change_todo),
]
