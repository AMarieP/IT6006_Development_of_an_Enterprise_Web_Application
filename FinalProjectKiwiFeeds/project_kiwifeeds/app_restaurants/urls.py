from django.urls import path
from .views import restaurant_list, restaurant_details

urlpatterns = [
   path("", restaurant_list, name="restaurant-list"),
   path("<int:restaurant_id>/", restaurant_details, name="restaurant-details"),
#    path("reviews/", review_list, name="review-list"),
#    path("review/<int:review_id>/", review_details, name="review-details"),
]