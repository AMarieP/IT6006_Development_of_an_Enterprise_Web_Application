from django.db import models
import os

# Create your models here.
def get_food_image_upload_path(instance, filename):
    # Get the restaurant ID and image number
    restaurant_id = instance.restaurant.id

    # Construct the upload path: 'Restaurant/restaurant_id/food_image/food_id.jpg'
    return os.path.join('Restaurant', str(restaurant_id), 'food_image', f'{instance.id}.jpg')

class Food(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=300)
    food_picture = models.ImageField(
        default='/profile_pics/temp_pfp_placeholder_REPLACE_LATER.avif',
        upload_to=get_food_image_upload_path,
        height_field=None,
        width_field=None
    )
    food_price = models.DecimalField(max_digits=5, decimal_places=2)
    restaurant = models.ForeignKey('app_restaurants.Restaurant', on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return self.name

    # permission denied , need to change user permission 
    # def save(self, *args, **kwargs):
        # Check if the Food instance has an ID (i.e., it's already saved)
        if not self.id:
            # If the ID is not generated, save the instance to generate an ID
            super(Food, self).save(*args, **kwargs)

        # Now that the ID is generated, set the food_picture upload path
        self.food_picture.name = get_food_image_upload_path(self, self.food_picture.name)

        # Save the file with the correct name
        self.food_picture.save(os.path.basename(self.food_picture.name), self.food_picture, save=False)

        # Save the instance again
        super(Food, self).save(*args, **kwargs)
