# Generated by Django 4.2.5 on 2023-09-24 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_food', '0007_food_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='slug',
        ),
    ]