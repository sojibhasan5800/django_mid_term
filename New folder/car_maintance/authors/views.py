from django.shortcuts import render,redirect,get_list_or_404
from .forms import registration_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from car_app.models import Car,brand_catagory
# Create your views here.
def registerpage(request):
    if request.method =='POST':
        register_form = registration_form(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            print(register_form.cleaned_data)
            return redirect('home_page')
    else:
        register_form = registration_form()
    return render(request,'register.html',{'formss':register_form,'type':'Register'})

from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def loginpage(request):
    if request.user.is_authenticated:
        return redirect("profile_page")
    
    nexts_url = request.GET.get('next', '/profile_page/')
    if not nexts_url:
        return redirect('profile_page')

    show_register = False  # ভুল হলে রেজিস্ট্রেশন বাটন দেখাবে

    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        
        # Clear the default error messages
        login_form.errors.clear()

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                messages.success(request, 'Login Successfully!')
                login(request, user)
                return redirect(nexts_url)
            else:
                # Only display custom error message
                messages.warning(request, 'Invalid username or password!')  # Toast message
                login_form.add_error(None, "❌ Invalid username or password!")  # Custom error
                show_register = True  
 
    else:
        login_form = AuthenticationForm()
    return render(request, 'register.html', {'formss': login_form, 'type': 'Login', 'show_register': show_register})

def postdetailspage(request,id):
    cars = Car.objects.get(pk=id)

    if request.method == 'POST':
       if not request.user.is_authenticated:
        messages.warning(request, 'You must be logged in to buy a car!')
        return redirect(f"/login_form/?next=/postdetails_page/{id}/")  # ✅ ঠিক URL দিন

   
       if cars.qunity != 0 :
           print(cars)
           cars.qunity-=1
           cars.save()
           messages.success(request,  f'Car: {cars.car_name} bought successfully!')
           request.user.profile_database.purchased_cars.add(cars)
           print("User is not authenticated!")
           return redirect('profile_page')
       else:
           messages.error(request, f'Car: {cars.car_name} is out of stock!')
           return redirect('postdetails_page')

    else:
        print("User is not authenticated!")
        return render(request,'details.html', {'data':[cars]})
    


@login_required
def profilepage(request):
    # if request.user.is_authenticated:
    #     return redirect("profile_page")

    users = request.user
    purchased_cars = users.profile_database.purchased_cars.all() 
    return render(request, 'profile.html', {'user': users, 'purchased_cars': purchased_cars})

    


@login_required
def logoutpage(request):
    logout(request)
    return redirect("home_page")

def catagorypage(request,slug):
    brand = get_list_or_404(brand_catagory,slug=slug)
    cars = Car.objects.filter(brand_name = brand)
    return render(request,'main_temp/base.html', {'data':cars})










