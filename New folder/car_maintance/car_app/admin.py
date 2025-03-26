from django.contrib import admin
from .models import brand_catagory,Car

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('brand_name',)}
    list_display = ['brand_name', 'slug']
    
admin.site.register(brand_catagory,CategoryAdmin)
admin.site.register(Car)
