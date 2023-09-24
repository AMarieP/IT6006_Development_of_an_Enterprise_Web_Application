from django.db import models
import os
from django.utils.text import slugify

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
    restaurant = models.ForeignKey('app_restaurants.Restaurant', on_delete=models.PROTECT)
    
    
    food_picture = models.ImageField(
        # default='/profile_pics/temp_pfp_placeholder_REPLACE_LATER.avif',
        upload_to=get_food_image_upload_path,
        height_field=None,
        width_field=None
    )
  

    def __str__(self) -> str:
        return self.name

    # permission denied , need to change user permission 
    #  # Override the save method to customize the food_picture field
    # def save(self, *args, **kwargs):
    #     # Check if the Food instance has an ID (i.e., it's already saved)
    #     if not self.id:
    #         super(Food, self).save(*args, **kwargs)  # Save to generate an ID if not already saved

    #     # Now that the ID is generated, set the food_picture upload path
    #     self.food_picture.name = get_food_image_upload_path(self, self.food_picture.name)

    #     # Save the file with the correct name
    #     self.food_picture.storage.save(self.food_picture.name, self.food_picture)

    #     super(Food, self).save(*args, **kwargs)  # Save the instance again
