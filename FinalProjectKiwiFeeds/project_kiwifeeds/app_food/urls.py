from django.urls import path
from django.contrib.auth import views
from.views import *

urlpatterns = [
    path("food/add-food/",views.CreateFood,name="add-food"),
    path("food/<int:pk>/",views.ViewFoodList,name="view-food"),
    path("food/<int:pk>/edit-food",views.EditFood,name="edit-food"),
    path("food/<int:pk>/delete-food",views.DeleteFood,name="delete-food"),
]