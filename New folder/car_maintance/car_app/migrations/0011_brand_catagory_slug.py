# Generated by Django 5.1.4 on 2025-03-20 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0010_remove_brand_catagory_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand_catagory',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
