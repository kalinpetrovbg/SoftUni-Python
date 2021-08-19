from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from VisitTurkey.website.forms import PlaceForm
from VisitTurkey.website.models import Place


def index(request):
    all_places = Place.objects.all().order_by('id')[::-1]
    count_places = len(all_places)
    if count_places >= 3:
        places = all_places[:3]
    else:
        places = Place.objects.all()
    context = {'places': places}
    return render(request, 'index.html', context)


def place_details(request, pk):
    place = Place.objects.get(pk=pk)
    is_owner = place.user == request.user
    context = {'place': place, 'is_owner': is_owner,}

    return render(request, 'details.html', context)


class UpdatePlace(LoginRequiredMixin, UpdateView):
    template_name = 'edit.html'
    model = Place
    form_class = PlaceForm
    success_url = reverse_lazy('home page')


class DeletePlace(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = Place
    success_url = reverse_lazy('home page')


class AllPlaces(ListView):
    template_name = 'places.html'
    model = Place
    context_object_name = 'places'
    paginate_by = 6


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
