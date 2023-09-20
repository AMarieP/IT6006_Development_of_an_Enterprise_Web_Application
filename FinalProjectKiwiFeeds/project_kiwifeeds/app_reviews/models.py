from django.db import models
from django.contrib.auth.models import User
from project_kiwifeeds.app_restaurants.models import Restaurant



# Create your models here.
class Review(models.Model):
   ONE_TO_FIVE_STAR_RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
   )

   user = models.ForeignKey(User, on_delete=models.PROTECT)
   restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
   rating = models.IntegerField(choices=ONE_TO_FIVE_STAR_RATING_CHOICES)
   review = models.TextField()