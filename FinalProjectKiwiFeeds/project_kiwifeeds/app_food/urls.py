from django.urls import path
from django.contrib.auth import views
from .views import *

urlpatterns = [
    path("food/add-food/", CreateFood,name="add-food"),
    #TODO: View Food List View Does Not Exist
    # path("food/<int:pk>/", ViewFoodList, name="view-food"),
    path("food/<int:pk>/edit-food", EditFood,name="edit-food"),
    path("food/<int:pk>/delete-food", DeleteFood, name="delete-food"),
]