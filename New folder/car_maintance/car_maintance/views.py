from django.shortcuts import render,redirect
from car_app.models import Car

def homepage(request):
    data = Car.objects.all()
    print(data)
    return render(request,'main_temp/base.html', {'data':data})



