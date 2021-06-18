from django.shortcuts import render, redirect

from petstagram.pets.models import Pet, Like


def pet_landing_page(request):
    return render(request, 'landing_page.html')

def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.like_count = pet.like_set.count
    context = {
        'pet': pet,
    }
    return render(request, 'pet_detail.html', context)

def pet_list(request):
    all_pets = Pet.objects.all()
    context = {
        'pets': all_pets,
    }
    return render(request, 'pet_list.html', context)

def pet_like(request, pk):
    pet_to_like = Pet.objects.get(pk=pk)
    like = Like(pet=pet_to_like)
    like.save()
    return redirect('pet details', pet_to_like.id)
