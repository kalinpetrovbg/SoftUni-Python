WORKSHOP 2 - PETSTAGRAM v2

1.	Създаваме нов app чрез create app pets и правим стандартните неща в началото.
2.	В models.py добавяме класове за Pet и за Like
class Pet(models.Model):
    TYPE_CHOICE_CAT = 'cat'
    TYPE_CHOICE_DOG = 'dog'
    TYPE_CHOICE_PARROT = 'parrot'
    TYPE_CHOICES = ((TYPE_CHOICE_CAT, 'cat'), (TYPE_CHOICE_DOG, 'dog'), (TYPE_CHOICE_PARROT, 'parrot'))
    type = models.CharField(max_length=6, choices=TYPE_CHOICES)
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image_url = models.URLField()
class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE) 
3.	Отиваме в admin.py и там добавяме 3 от полетата да са видими чрез:
from petstagram.pets.models import Pet
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'age']
admin.site.register(Pet, PetAdmin)
4.	След като имаме модела – трябва да си създадем вютата. Импортваме първо класа Pet
from petstagram.pets.models import Pet
и след това създаваме 4 функции за 4-те основни страници:
def pet_landing_page(request): pass
def pet_details(request): pass
def pet_landing_page(request): pass
def pet_like(request): pass
5.	А pet_list функцията пишем следното, за да визуализираме темплейта:
def pet_list(request):
    all_pets = Pet.objects.all()
    context = {
        'pets': all_pets,
    }
    return render(request, 'pet_list.html', context)
Така чрез Pet.objects.all() ще покажем всички обекти Pet.
6.	А в pet.details функцията пишем следното:
def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    context = {
        'pet': pet,
    }
    return render(request, 'pet_detail.html', context)
Тук с objects.get(pk=pk) ще покажем само животното с определения прайвът ключ
7.	След като имаме модела, имаме и вютата им, трябва да ги вържем с линкове. За целта във файла pets > urls.py импортваме фукнциите от views.py
from petstagram.pets.views import pet_details, pet_list, pet_landing_page
И след това добавяме path към тях:
urlpatterns = [
    path('', pet_list, name='list pets'),
    path('index/', pet_landing_page, name='landing page'),
    path('details/<int:pk>', pet_details, name='pet details'),
]
8.	Трябва да влезем и да редактираме също и темплейта pet_list.html
Като добавим for цикъл за pet in pets, както и pets.атрибутите, които искаме да се покажат.
{% for pet in pets %}
            <div class="col-lg-4">
                <div class="card" style="width: 18rem;">
                    <img src="{{ pet.image_url }}" class="card-img-top" alt="image of {{ pet.name}}" />
                    <div class="card-body">
                        <h5 class="card-title">{{ pet.name }}, {{ pet.age }}</h5>
                        <p class="card-text">{{ pet.description }}</p>
                        <a href="{% url 'pet details' pet.id %}" class="btn btn-primary">See details</a>
                    </div>
                </div>
            </div>
{% endfor %}
Като за да добавим URL, който да води към pet_details сме добавили не само name-а на URL-а, но и сме добавили pet.id след него. По този начин ще вържем бутона See details с URL като това: ../pets/details/1
9.	Добавяме си необходимите pet.атрибути на необходимите места и в pet_detail.html. И всичко би трябвало да работи, без Like бутона. За целта в темплейта pet_details.html добавяме {{ pet.likes_count }} и във вюто на def pet_details добавяме променлива, която ще отчита броя лайкове чрез кода
    pet.like_count = pet.like_set.count()   (или без скобите отзад)
10.	За да визуализираме в админ частта лайковете отиваме в admin.py и създаваме метод на класа PetAdmin, тоест фукция, на който подаваме обекта и след това добавяме в list_display като параметър тази фунция:
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'age', 'likes_counter']
    def likes_counter(self, obj):
        return obj.like_set.count()
11.	Накрая правим опция да се лайкват животните. Влизаме в views.py и модифицираме функцията def pet_like
def pet_like(request, pk):
    pet_to_like = Pet.objects.get(pk=pk)
    like = Like(pet=pet_to_like)
    like.save()
    return redirect('pet details', pet_to_like.id)
12.	След това добавяме в urls.py път.   path('like/<int:pk>', pet_like, name='pet_like')
13.	И добавяме този url в темплейта pet_details.html  чрез {% url 'pet_like' pet.id %}
