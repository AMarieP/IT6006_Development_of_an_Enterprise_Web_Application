from django.urls import path

from .views import *

urlpatterns = [
    path("<int:restaurant_id>/add-food/", FoodCreateView.as_view(),name="add-food"),
    #TODO: View Food List View Does Not Exist
    path("", FoodList, name="view-food"),
    # path('<int:food_id>/edit-food/', FoodUpdateView.as_view(), name='edit-food'),
    path("<int:food_id>/edit-food", EditFood,name="edit-food"),
    path("<int:food_id>/delete-food", DeleteFood, name="delete-food"),
]