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
    current = Recipe.objects.get(pk=pk)
    context = {
        'recipe': current,
    }
    return render(request, 'edit.html', context)


def edit_btn(request, pk):
    current = Recipe.objects.get(pk=pk)

    title = request.POST['title']
    image_url = request.POST['image_url']
    description = request.POST['description']
    ingredients = request.POST['ingredients']
    time = request.POST['time']

    form = Recipe(title=title, image_url=image_url, description=description, ingredients=ingredients, time=time)

    if form.title == current.title and \
            form.image_url == current.image_url and\
            form.description == current.description and \
            form.ingredients == current.ingredients and \
            form.time == current.time:
        form.save()
    else:
        current.title = title
        current.image_url = image_url
        current.description = description
        current.ingredients = ingredients
        current.time = time
        current.save()

    return redirect('/')


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
