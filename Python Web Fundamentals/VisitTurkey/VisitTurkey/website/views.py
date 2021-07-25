from django.shortcuts import render, redirect

from VisitTurkey.website.forms import PlaceForm
from VisitTurkey.website.models import Place


def home_page(request):
    return render(request, 'index.html')


def place_details(request, pk):
    pass

def all_places(request):
    places = Place.objects.all()
    context = {'places': places}

    return render(request, 'places.html', context)


# @login_required
def create_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # pet = form.save(commit=False)
            # pet.user = request.user
            # pet.save()
            return redirect('home page')
    else:
        form = PlaceForm()

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)

