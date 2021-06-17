from django.contrib import admin

from todos_app.todos.models import Todo
from todos_app.todos.models.todo import Person, Category

class TodoAdmin(admin.ModelAdmin):
    list_display = ['name_of_task', 'owner']
    sortable_by = ['name_of_task']
    list_filter = ['owner']

class ChangedCategory(admin.ModelAdmin):
    list_display = ['name']

# Option one
admin.site.register(Todo, TodoAdmin)
admin.site.register(Person)
admin.site.register(Category, ChangedCategory)

""""
# Option two
# @admin.register(Todo) 
"""
