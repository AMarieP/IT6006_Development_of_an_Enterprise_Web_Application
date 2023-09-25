from django.db import models
from app_user.models import UserProfile
from app_restaurants.models import Restaurant

class Favorites(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name='fav_user')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT, related_name='fav_restaurant')