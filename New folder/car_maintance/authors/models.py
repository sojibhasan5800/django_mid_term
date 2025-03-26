from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from car_app.models import Car

class profile_database(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    purchased_cars = models.ManyToManyField(Car, blank=True)

    def __str__(self):
       return self.user.username


