from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Restaurant(models.Model):
    #restaurant_id
    restaurant_name = models.CharField(max_length=255)
    restaurant_owner = models.CharField(max_length=255)
    restaurant_description = models.CharField(max_length=255)
    restaurant_location = models.CharField(max_length=255)
    #user= models.OneToOneField(User, on_delete=models.Cascade,related_name='user')

    def __str__(self):
        return f'{self.restaurant_name} {self.restaurant_owner}'

class Review(models.Model):
    #review_id
    #restaurant_name = models.CharField(max_length=255)
    #rating
    title = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.PROTECT, related_name='restaurant')
    user = models.ForeignKey(User,on_delete=models.PROTECT, related_name='user')

    def __str__(self):
        return f'{self.comment} {self.user}'
    



