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
    
    nexts_url = request.GET.get('next') or 'profile_page'

    # if not nexts_url:
    #     return redirect('profile_page')

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
        return redirect(f"/author_page/login_form/?next=/author_page/postdetails_page/{id}/")  # ✅ ঠিক URL দিন

   
       if cars.qunity != 0 :
           print(cars)
           cars.qunity-=1
           cars.save()
           messages.success(request,  f'Car: {cars.car_name} bought successfully!')
           request.user.profile_database.purchased_cars.add(cars)
           return redirect('profile_page')
       else:
           messages.warning(request, f'Car: {cars.car_name} is out of stock!')
           return redirect('postdetails_page',id =id)

    else:
        return render(request,'details.html', {'data':[cars]})
    


# @login_required
# def profilepage(request):
#     users = request.user
#     purchased_cars = users.profile_database.purchased_cars.all() 
#     print(purchased_cars)
#     return render(request, 'profile.html', {'user': users, 'purchased_cars': purchased_cars})


# @login_required
# def profilepage(request):
#     users = request.user
#     profile = users.profile_database  # ইউজারের প্রোফাইল ডাটাবেজ
#     purchased_cars = profile.purchased_cars.all()  # ইউজার যে গাড়ি কিনেছে তা লোড করা

#     # যদি ইউজার কোনো গাড়ি ডিলিট করতে চায়
#     if request.method == 'POST' and 'delete_car_id' in request.POST:
#         car_id = request.POST['delete_car_id']
#         car_to_remove = Car.objects.get(id=car_id)
#         profile.purchased_cars.remove(car_to_remove)  # গাড়ি রিমুভ করা
#         messages.success(request, f'Removed {car_to_remove.car_name} from purchase history!')
#         return redirect('profile_page')
#     return render(request, 'profile.html', {'user': users, 'purchased_cars': purchased_cars})

@login_required
def profilepage(request):
    user = request.user
    profile = user.profile_database  # user's profile database
    purchased_cars = profile.purchased_cars.all()  # Cars purchased by the user

    if request.method == 'POST':
        # If deleting selected cars
        if 'delete_selected' in request.POST:
            car_ids_to_delete = request.POST.getlist('delete_car_ids')
            if car_ids_to_delete:
                for car_id in car_ids_to_delete:
                    car_to_remove = Car.objects.get(id=car_id)
                    profile.purchased_cars.remove(car_to_remove)
                messages.success(request, 'Selected cars have been removed from your purchase history!')
            else:
                messages.warning(request, 'No cars selected for deletion!')
            return redirect('profile_page')

        # If deleting all cars
        if 'delete_all' in request.POST:
            profile.purchased_cars.clear()
            messages.success(request, 'All cars have been removed from your purchase history!')
            return redirect('profile_page')

    return render(request, 'profile.html', {'user': user, 'purchased_cars': purchased_cars})


@login_required
def logoutpage(request):
    logout(request)
    return redirect("home_page")

def catagorypage(request,slug):
    brand = get_list_or_404(brand_catagory,slug=slug)
    cars = Car.objects.filter(brand_name = brand)
    return render(request,'main_temp/base.html', {'data':cars})










