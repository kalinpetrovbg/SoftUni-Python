from django.shortcuts import render, redirect

from recipes_app.rec.models import Recipe


def home_page(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)

def create_recipe(request):
    return render(request, 'create.html')

def create_new(request):
    title = request.POST['title']
    image_url = request.POST['image_url']
    description = request.POST['description']
    ingredients = request.POST['ingredients']
    time = request.POST['time']

    form = Recipe(title=title, image_url=image_url, description=description, ingredients=ingredients, time=time)
    form.save()
    return redirect('/')

def edit_recipe(request, pk):
    return render(request, 'edit.html')

def delete_recipe(request, pk):
    current = Recipe.objects.get(pk=pk)
    context = {
        'recipe': current
    }
    return render(request, 'delete.html', context)

def delete_item(request, pk):
    current = Recipe.objects.get(pk=pk)
    current.delete()
    return redirect('/')



def details(request, pk):
    context = {
        'recipe': Recipe.objects.get(pk=pk),
    }
    return render(request, 'details.html/', context)
