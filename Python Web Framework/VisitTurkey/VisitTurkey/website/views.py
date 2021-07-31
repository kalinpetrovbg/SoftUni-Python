from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from VisitTurkey.website.forms import PlaceForm, CommentForm
from VisitTurkey.website.models import Place
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, FormView


class IndexPage (ListView):
    template_name = 'index.html'
    model = Place
    context_object_name = 'places'
    paginate_by = 6


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


class UpdatePlace (UpdateView):  ### + AnyGroupRequiredMixin
    template_name = 'edit.html'
    model = Place
    fields = '__all__'
    context_object_name = "cake"
    success_url = reverse_lazy('home page')


class DeletePlace (DeleteView):   ### + AnyGroupRequiredMixin
    template_name = 'delete.html'
    model = Place
    success_url = reverse_lazy('home page')


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
