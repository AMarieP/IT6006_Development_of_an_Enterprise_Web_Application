from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserChangeForm

class UserProfileView(DeleteView):
    pass

class UserUpdateView(UpdateView):
    pass

class UserCreateView(CreateView):
    pass

class UserDeleteView(DeleteView):
    pass

#Login and Logout Using Django auth

class UserLoginView(LoginView):
    pass

class UserLogoutView(LogoutView):
    pass