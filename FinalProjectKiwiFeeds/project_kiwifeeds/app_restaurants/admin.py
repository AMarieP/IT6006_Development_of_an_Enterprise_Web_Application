from django.contrib import admin

from app_review.models import Restaurant, Review

# Register your models here.
admin.site.register(Review)
admin.site.register(Restaurant)