from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    this_user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to=None, height_field=None, width_field=None)
    phone_number = models.IntegerField(max_length=10)
    favourite_restaurants = models.ForeignKey()
