from django.db import models
from app_restaurant.models import Restaurant

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=255)
    discription = models.CharField(max_length=300)
    food_picture = models.ImageField(upload_to='profile_pics', height_field=None, width_field=None)
    food_price = models.DecimalField(max_digits=5, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name