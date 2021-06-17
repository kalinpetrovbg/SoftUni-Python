from django.shortcuts import render, redirect
from todos_app.todos.models import Todo
from todos_app.todos.models.todo import Person


def index(request):
    context = {
        'todos': Todo.objects.all(),
    }
    return render(request, 'index.html', context)

def create_todo(request):
    text = request.POST['name_of_task']
    description = request.POST['description']
    owner_name = request.POST['owner']

    owner = Person.objects.filter(name=owner_name).first()
    if not owner:
        owner = Person(name=owner_name)
        owner.save()

    todo = Todo(
        name_of_task=text,
        description=description,
        owner=owner,
    )

    todo.save()

    return redirect('/')


def delete_todo(request):
    search = request.POST['name']
    found = Todo.objects.filter(name_of_task=search).first()

    if found:
        found.delete()

    return redirect('/')

def change_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.status = not todo.status
    todo.save()

    return redirect('/')