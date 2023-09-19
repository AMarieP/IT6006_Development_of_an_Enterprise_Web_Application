from django.db import models

# Create your models here.
class Review(models.Model):
 #   user = models.ForeignKey()
 #  restaurant = models.ForeignKey()
    rating = models.IntegerField()
    review = models.TextField()