from django.shortcuts import render,redirect
from .forms import registration_form
from django.contrib import messages

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


