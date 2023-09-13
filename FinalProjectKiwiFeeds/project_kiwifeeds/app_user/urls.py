from django.urls import path
from .views import UserCreateView, UserDeleteView, UserProfileView, UserUpdateView

urlpatterns = [
    path("signup/", UserCreateView.as_view(), name="signup"),
    path("profile-page/", UserProfileView.as_view(), name="profile-page"),
    path("delete-account/", UserDeleteView.as_view(), name="delete-account"),
    path("edit-profile/", UserUpdateView.as_view(), name="edit-profile"),


]