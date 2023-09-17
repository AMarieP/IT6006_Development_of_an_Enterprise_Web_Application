from django.contrib import admin

from app_restaurants.models import Restaurant, Review

# Register your models here.
admin.site.register(Review)
admin.site.register(Restaurant)