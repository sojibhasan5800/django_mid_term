# Generated by Django 5.1.4 on 2025-03-20 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0008_alter_brand_catagory_brand_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand_catagory',
            name='brand_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
