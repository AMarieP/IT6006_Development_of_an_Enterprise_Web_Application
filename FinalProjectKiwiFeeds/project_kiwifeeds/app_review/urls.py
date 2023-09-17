from django.urls import path
from .views import restaurant_list, review_list, review_details
from . import views

urlpatterns = [
   #path("",review_list ,name="home"),
   #path("reviews/", review_list, name="reviewlist"),
   path("reviews/", review_list, name="review-list"),
   path("review/<int:review_id>/", review_details, name="review-details"),
   path("restaurants/", restaurant_list, name="restaurants-list")
]