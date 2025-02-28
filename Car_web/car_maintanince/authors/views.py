from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def registerpage(request):
    if request.method == 'POST':
        print(100)
        register_form = RegistrationForm(request.POST)  # Fixed form initialization
        if register_form.is_valid():
            messages.success(request, 'Account created successfully')
            messages.info(request, 'Welcome')
            messages.warning(request, 'This is a warning message')
            print(10)
            
            register_form.save()
            return redirect('signup_page')  # Redirect after successful registration
    else:
        register_form = RegistrationForm()  # Correctly indented

    return render(request, 'register.html', {'form': register_form, 'type': 'Register'})
