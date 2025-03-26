from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class registration_form(UserCreationForm):
     
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None  
        self.fields['password2'].help_text = None
        
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-controls'}) 
                             ,error_messages={'required': "Emails is required.", 'invalid': "Enter a valid email address."})   
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-controls'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels={
            'username':'user_Name',
        }
        help_texts={
            'username':'usernameMust Be fields @@/*-',
          
        }
        error_messages = {
                    'username': {
                        'required': "Usernames is requireds.",  # When left empty
                        'unique': "This username is already taken.",  # When a duplicate username is entered
                        'invalid': "Enter a valid username."  # If username contains invalid characters
                    },
                    
                }



        