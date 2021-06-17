Models

1.	В файла models.py пишем
class Todo(models.Model): 
text = models.CharField(max_length=30)
2.	Пишем makemigrations за да генерираме миграция с новата база. Може да се наложи да напишем и името на app-a, ако не го намери. След това пишем migrate. 
3.	За да сложим models в папка, а не като файл, създаваме пакет models в главната папка . В нея слагаме и models.py файла, като можем да си го прекръстим на todo.py. 
4.	За да сработи папката models, трябва да импортнем в __init__ файла ѝ from .todo import Todo (това е класа, който сме си създали в models.py). След това даваме makemigrations.
5.	За да направим релационна връзка между две таблици – правим в todo.py един нов клас class Person(models.Model):
name = models.CharField(max_length=30)
и добавяме към класа Todo един нов ред
owner = models.ForeignKey(към кой обект, on_delete=models.CASCADE, null=True)
description = models.TextField(null=True, blank=True)
6.	В admin.py регистрираме моделите, които искаме да се показват като пишем
from todos_app.todos.models import Todo
admin.site.register(Todo)                           Save-ваме файла и презареждаме админската част.
7.	Правим същото и за другия клас Person, който е свързан с Todo и импорта е леко по-различен (наследява Todo)
from todos_app.todos.models.todo import Person
admin.site.register(Person)
8.	Ако имаме проблем с наименуванието в множествено число в админа (напр. Persons). Отивамe в todo.py и в съответния проблемен клас добавяме следното под атрибута
class Meta:
verbose_name_plural = ‘people’     и ще стане (People).
9.	Можем да добавим в класа People (файла todo.py), за да ни излиза по хубав начин в drop-down-a при селектиране това 
def __str__(self):
return f"{self.id}: {self.name}"
10.	Можем и да отидем в admin.py и да създадем нов клас, който да промени изгледа на списъка със задачи
class TodoAdmin(admin.ModelAdmin):
    list_display = ['text', ‘owner’]
като в същото време добавяме новия клас в admin.site.register-a след Todo
admin.site.register(Todo, TodoAdmin)
11.	В същият файл admin.py можем да добавим и още неща на TodoAdmin класа
sortable_by = [‘text’]  (text в случая е променливата в класа, може да е различно от text)
list_filter = [‘owner’]
12.	За да се добави избор от падащо меню за някой клас в todo.py пишем следното
HOME_CHOICE = ‘Home’
WORK_CHOICE = ‘Work’
NAME_CHOICES = ((HOME_CHOICE, ‘Home stuff‘),(WORK_CHOICE, ‘Work stuff’))
и добавяме това към съответния CharField:
choices=NAME_CHOICES
По този начин създаваме полетата първо за базата, а след това ги създаваме за потребителя. 


MTV Patterns

1.	За да съзададем първото си view, пишем следното във файла todos > views.py
def index(request):
    pass
2.	Във файла todos > urls.py създаваме нов URL в списъка urlpatterns и импортваме view-то.
from todos_app.todos.views import index
urlpatterns = [path('', index)]
3.	За да визуализираме данните от нашата база, заменяме pass от views.py с
contex = {‘todos’: []}
return render(reques, ‘index.html’, context)
4.	Създаваме index.html файла в templates, в който пишем:
{% for todo in todos %}
{{  todo }}
{% endfor %}
5.	След това в views.py променяме [] на: Todo.objects.all()  Трябва да импортем и модела:
from todos_app.todos.models import Todo
По този начин можем да визуализираме данни от нашата база директно в html страницата.


Create and Delete Forms

1.	За да направим форма, която да добавя потребители, трябва да я създадем в темплейта ни index.html.
    <form method="post" action="todos-add">
{% csrf_token %}
        <input type="text" name="name" />
        <textarea name="description"></textarea>
        <input type="text" name="owner" />
        <button>Create</button>
    </form>
2.	След това отиваме в urls.py файла и добавяме пътя към todos-add, като създаваме и път към фунцкцията create_todo.
urlpatterns = [path('todos-add', create_todo),]
3.	Отиваме във views.py и добавяме def create_todo(request):  pass.  Няма да слагаме темплейт, а сами ще напишем тук бизнес логиката.
4.	Връщаме се в urls.py и импортваме новосъздадената функция.
5.	Обратно в views.py добавяме: 
from django.shortcuts import render, redirect
from todos_app.todos.models.todo import Person
def create_todo(request):
    text = request.POST['name']
    description = request.POST['description']
    owner_name = request.POST['owner']
    owner = Person.objects.filter(name=owner_name).first()
    if not owner:
        owner = Person(name=owner_name)
        owner.save()
    todo = Todo(
        name=text,
        description=description,
        owner=owner,)
    todo.save()
    return redirect('/') 
6.	За да изтрием todo - създаваме функция (бизнес логиката), която ще трие todo-тата във views.py:
def delete_todo(request):
    search = request.POST['name']
    found = Todo.objects.filter(name=search).first()
    if found:
        found.delete()
    return redirect('/')      тоест, ако намериш сред обектите Todo нашият search, изтрий го.
7.	Добавяме urlspattern в urls.py и импортваме функцията, която създадогме във views.py.
from todos_app.todos.views import delete_todo
path('todos-del', delete_todo),
8.	Във файла index.html добавяме самата логика на темплейта:
    <form method="post" action="todos-del">
        {% csrf_token %}
        <label>Delete tasks</label>
        <input type="text" name="name">
        <button>Delete Task</button>
    </form>
9.	За да променим статуса на някоя от задачите, отиваме и създаваме във view.py функцията change_todo:
def change_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.status = not todo.status
    todo.save()
    return redirect('/')
10.	След това добяваме пътя в urls.py и я импортваме:
from todos_app.todos.views import change_todo
    path('todo-change/<int:pk>', change_todo),
11.	Накрая в темплейта визуализираме бутон, който да сменя статуса и да извиква модула.
            <form method="post" action="/todo-change/{{ todo.id }}">
                {%  csrf_token %}
                {% if todo.status %}
                    <input type="hidden" name="status" value="false" />
                    <div class="done">DONE</div>
                        <button>Change</button>
                {% else %}
                    <input type="hidden" name="status" value="true" />
                    <div class="open">NOT DONE</div>
                        <button>Change</button>
                {% endif %}
            </form>
