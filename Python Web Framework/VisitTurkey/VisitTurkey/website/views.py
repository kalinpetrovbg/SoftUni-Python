from django.shortcuts import render, redirect

from VisitTurkey.website.forms import PlaceForm, CommentForm
from VisitTurkey.website.models import Place


def home_page(request):
    return render(request, 'index.html')


def place_details(request, pk):
    place = Place.objects.get(pk=pk)
    is_owner = place.user == request.user
    comments = place.comment_set.all()
    context = {'place': place, 'is_owner': is_owner, 'comments': comments}

    return render(request, 'details.html', context)


# @login_required
def create_comment(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()

    return redirect('place details', pk)


def delete_place(request):
    pass


def edit_place(request):
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
            place = form.save(commit=False)
            place.user = request.user
            place.save()

            return redirect('all places')
    else:
        form = PlaceForm()

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)
