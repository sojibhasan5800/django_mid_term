# Generated by Django 5.1.4 on 2025-03-25 06:20

import car_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0012_alter_car_car_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_images',
            field=models.ImageField(default='core/images/im.jpeg', upload_to=car_app.models.car_image_upload_path),
        ),
    ]
