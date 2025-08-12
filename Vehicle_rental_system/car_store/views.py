from django.shortcuts import render
from django.http import HttpResponse
from .models import Cars

def index(request):
    cars = Cars.objects.all()
    return HttpResponse(", ".join([car.model for car in cars]))


""" def car_detail(request, car_id):
    try:
        car = Cars.objects.get(id=car_id)
        return HttpResponse(f"Car: {car.model}, Year: {car.year}, Price: {car.price}")
    except Cars.DoesNotExist:
        return HttpResponse("Car not found", status=404) """

def home_view(request):
    context = {'name': 'Kibe'}  # Data to pass into the template
    return render(request, 'home.html', context)