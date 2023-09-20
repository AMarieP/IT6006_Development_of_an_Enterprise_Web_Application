# Generated by Django 4.2.4 on 2023-09-20 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('discription', models.CharField(max_length=300)),
                ('food_picture', models.ImageField(upload_to='profile_pics')),
                ('food_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_restaurants.restaurant')),
            ],
        ),
    ]
