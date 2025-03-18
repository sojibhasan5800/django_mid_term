from django.shortcuts import render,redirect
from .forms import registration_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

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

def loginpage(request):
    if request.user.is_authenticated:
        return redirect("profile_page")
    
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username = user_name, password= user_pass)
            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('profile_page')
            else:
                print(10)
                messages.warning(request, 'Login informtion incorrect')
                return redirect('login_page')
    
        messages.error(request, "Invalid usernames or password")
        return redirect('login_page')
            
    else:
        login_form = AuthenticationForm()
        return render(request,'register.html',{'formss':login_form,'type':'Login'})
    
@login_required
def profilepage(request):
    data = request.user
    return render(request,'profile.html',{'data':data})

@login_required
def logoutpage(request):
    logout(request)
    return redirect("home_page")


