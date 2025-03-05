
from django.urls import path

from .views import registerpage
urlpatterns = [
   path('registration_form/',registerpage,name="signup_page")
]
