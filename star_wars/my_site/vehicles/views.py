from django.shortcuts import render
from .models import Vehicles

def index(request):
    veh = Vehicles.objects.all()
    context = {
        "vehicles": veh
    }
    return render(request, 'vehicles/v_index.html', context)

def details(request, vehicle_id):
    veh = Vehicles.objects.filter(id=vehicle_id).first()
    context = {
        "vehicle": veh
    }
    return render(request, 'vehicles/v_details.html', context)