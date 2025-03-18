
from django.urls import path

from .views import registerpage,profilepage,loginpage,logoutpage
urlpatterns = [
   path('registration_form/',registerpage,name="signup_page"),
   path('login_form/',loginpage,name="login_page"),
   path('logout_form/',logoutpage,name="logout_page"),
   path('profile_page/',profilepage,name="profile_page"),

]
