from django.db import models
import os
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
def get_food_image_upload_path(instance, filename):
    # Get the restaurant ID and image number
    # restaurant_id = instance.restaurant.id

    # Construct the upload path: 'Restaurant/restaurant_id/food_image/food_id.jpg'
    return os.path.join('restaurant', 'food_image', filename)

class Food(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=300)
    food_price = models.DecimalField(max_digits=5, decimal_places=2)
    restaurant = models.ForeignKey('app_restaurants.Restaurant', on_delete=models.PROTECT,related_name='food')
    
    
    food_picture = models.ImageField(
        # default='/profile_pics/temp_pfp_placeholder_REPLACE_LATER.avif',
        upload_to=get_food_image_upload_path,
        height_field=None,
        width_field=None
    )
  

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
      return reverse('food', kwargs={'pk': self.pk})

