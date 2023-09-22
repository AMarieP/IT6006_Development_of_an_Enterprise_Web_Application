from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Review(models.Model):
   ONE_TO_FIVE_STAR_RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
   )

   # user and restaurant will be protected if we delete any review
   user = models.ForeignKey('app_user.UserProfile', on_delete=models.PROTECT)
   restaurant = models.ForeignKey('app_restaurants.Restaurant', on_delete=models.PROTECT)
   rating = models.IntegerField(choices=ONE_TO_FIVE_STAR_RATING_CHOICES)
   comment = models.TextField()

   def get_absolute_url(self):
      return reverse('review', kwargs={'pk': self.pk})