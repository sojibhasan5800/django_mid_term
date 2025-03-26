from django.shortcuts import render,redirect
from car_app.models import Car

def homepage(request):
    data = Car.objects.all()
    for car in data:
       print(f"Car Name: {car.car_name}, Image Path: {car.car_images.url}")
    return render(request,'main_temp/base.html', {'data':data})



