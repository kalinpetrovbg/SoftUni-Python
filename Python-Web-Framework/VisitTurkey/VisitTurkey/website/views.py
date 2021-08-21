from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView

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


class PlaceDetails(DetailView):
    template_name = 'details.html'
    model = Place
    context_object_name = 'place'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        place = context['place']
        is_owner = place.user == self.request.user
        context['is_owner'] = is_owner
        return context


class CreatePlace(CreateView):
    template_name = 'create.html'
    model = Place
    form_class = PlaceForm
    success_url = reverse_lazy('all places')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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
