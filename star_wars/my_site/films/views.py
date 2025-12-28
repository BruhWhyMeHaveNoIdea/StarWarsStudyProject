from django.shortcuts import render
from .models import Films

def index(request):
    films = Films.objects.all()
    context = {'films': films}
    return render(request, 'films/f_index.html', context)

def details(request, film_id):
    films = Films.objects.filter(id=film_id).first()
    context = {'film': films}
    return render(request, 'films/f_details.html', context)