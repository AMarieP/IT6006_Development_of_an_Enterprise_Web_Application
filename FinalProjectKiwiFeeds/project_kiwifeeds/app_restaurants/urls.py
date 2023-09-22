from django.urls import path
from .views import restaurant_list, restaurant_details, RestaurantCreateView, RestaurantEditView, RestaurantDeleteView

urlpatterns = [
   path("", restaurant_list, name="restaurant-list"),
   path("<int:restaurant_id>/", restaurant_details, name="restaurant-details"),
   path("create/", RestaurantCreateView, name="create-restaurant"),
   path("<int:restaurant_id>/edit/", RestaurantEditView, name="edit-restaurant"),
   path("<int:restaurant_id>/delete/", RestaurantDeleteView, name="delete-restaurant"),

]