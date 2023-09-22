from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=255)
    restaurant_description = models.CharField(max_length=255)
    restaurant_location = models.CharField(max_length=255)
    # Restaurant Owner is one-to-one relationship with userProfile
    restaurant_owner = models.ForeignKey('app_user.UserProfile',on_delete=models.PROTECT, related_name='user',null=True,blank=True)
    def __str__(self):
        return f'{self.restaurant_name}, owned by {self.restaurant_owner}'





