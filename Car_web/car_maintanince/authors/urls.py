from django.urls import path
from .views import registerpage

urlpatterns = [
   path('signup/',registerpage,name='signup_page')
]