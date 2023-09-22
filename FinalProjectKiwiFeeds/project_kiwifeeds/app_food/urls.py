from django.urls import path
from django.contrib.auth import views
from .views import *

urlpatterns = [
    path("add-food/", CreateFood,name="add-food"),
    #TODO: View Food List View Does Not Exist
    path("", FoodList, name="view-food"),
    path("<int:food_id>/edit-food", EditFood,name="edit-food"),
    path("<int:food_id>/delete-food", DeleteFood, name="delete-food"),
]