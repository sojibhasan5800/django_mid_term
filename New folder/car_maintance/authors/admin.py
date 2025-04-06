from django.contrib import admin
from .models import profile_database
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    exclude = ('purchased_cars',) 
    readonly_fields=('display_purchased_cars',)

    def display_purchased_cars(self, obj):
        cars = obj.purchased_cars.all()
        if not cars:
            return "No cars purchased"
        return "\n".join([f"- {car.car_name}" for car in cars])
    display_purchased_cars.short_description = 'Purchased Cars'
    
admin.site.register(profile_database,ProfileAdmin)