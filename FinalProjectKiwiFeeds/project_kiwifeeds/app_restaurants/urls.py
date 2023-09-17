from django.urls import path
from .views import restaurant_list, review_list, review_details
from . import views

urlpatterns = [
   #path("",review_list ,name="home"),
   #path("reviews/", review_list, name="reviewlist"),
   path("restaurants/", restaurant_list, name="restaurant-list"),
   path("restaurant/<int:restaurant_id>/", restaurant_details, name="restaurant-details"),
   path("reviews/", review_list, name="review-list"),
   path("review/<int:review_id>/", review_details, name="review-details"),
]