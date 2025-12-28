from django.shortcuts import render
from .models import Spaceships

def index(request):
    ships = Spaceships.objects.all()
    context = {
        'ships': ships
    }
    return render(request, 'ships/s_index.html', context)

def details(request, ship_id):
    ships = Spaceships.objects.filter(id=ship_id).first()
    context = {
        'ship': ships
    }
    return render(request, 'ships/s_details.html', context)