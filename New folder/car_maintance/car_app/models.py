from django.db import models
from django.utils.text import slugify

def car_image_upload_path(instance, filename):
    """ যদি ইউজার ছবি আপলোড করে তাহলে car_app/cars_images/ তে যাবে,
        অন্যথায় BASE_DIR/im.jpeg থাকবে। """
    
    if filename:  # যদি ইউজার ইমেজ আপলোড করে
        return f'car_app/media/cars_images/{filename}'
    return 'core/images/im.jpeg'  # ডিফল্ট ইমেজ (BASE_DIR/im.jpeg)

# Create your models here.
class brand_catagory(models.Model):
    brand_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    def __str__(self):
        return f"Brand: {self.brand_name}"


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    car_price = models.IntegerField()
    brand_name = models.ForeignKey(brand_catagory,related_name="brand_cat", on_delete=models.CASCADE)
    car_images = models.ImageField(upload_to=car_image_upload_path, default='core/images/im.jpeg')
    qunity = models.IntegerField(default=0)
    description = models.TextField(default='Nothing_details')
    def __str__(self):
        return f"car_name : {self.car_name}"







