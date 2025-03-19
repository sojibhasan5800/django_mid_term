from django.db import models

# Create your models here.
class brand_catagory(models.Model):
    brand_name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return f"Brand: {self.brand_name}"

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    car_price = models.IntegerField()
    brand_name = models.ForeignKey(brand_catagory,related_name="brand_cat", on_delete=models.CASCADE)
    car_images = models.ImageField(upload_to='car_app/static/cars_images/', default='images/im.jpeg')
    qunity = models.IntegerField(default=0)
    description = models.TextField(default='Nothing_details')
    def __str__(self):
        return f"car_name : {self.car_name}"







