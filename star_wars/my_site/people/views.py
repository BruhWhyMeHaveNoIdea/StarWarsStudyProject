from django.shortcuts import render, get_object_or_404
from .models import People

def index(request):

    people = People.objects.all()
    context = {
        'people': people  # Person.objects.all() когда будет модель
    }
    return render(request, 'people/p_index.html', context)

def details(request, person_id):
    person = People.objects.filter(id=person_id).first()
    context = {
        'person': person
    }
    return render(request, 'people/p_details.html', context)