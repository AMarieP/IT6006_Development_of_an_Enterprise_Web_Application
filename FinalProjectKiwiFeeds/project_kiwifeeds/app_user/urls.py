from django.urls import path
from django.contrib.auth import views
from .views import *

urlpatterns = [
    path("signup/", UserCreateView.as_view(), name="signup"),
    path("signup-business/", BusinessUserCreateView.as_view(), name="signup-business"),
    path("<int:pk>/", UserProfileView.as_view(), name="profile-page"),
    path("<int:pk>/delete-account/", UserDeleteView.as_view(), name="delete-account"),
    path("<int:pk>/edit-profile/", UserUpdateView.as_view(), name="edit-profile"),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    # path('change-password/', UserChangePassword.as_view(), name='change-password'),
    # path('change-success/', UserPasswordChangeDone.as_view(), name='change-success')

]

#TO DO: Add profile deleted sucess template as a page