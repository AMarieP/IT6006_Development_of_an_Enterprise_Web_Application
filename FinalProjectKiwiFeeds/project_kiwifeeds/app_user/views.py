from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from models import UserProfile

class UserProfileView(DetailView):
    model = UserProfile
    fields = ['profile_picture', 'phone_number']
    template_name = 'user_profile_page.html'

class UserUpdateView(UpdateView):
    model = UserProfile
    fields = ['profile_picture', 'phone_number']
    success_url = reverse_lazy('profile-page')
    template_name = 'user_profile_edit.html'


class UserCreateView(CreateView):
    model = UserProfile
    fields = ['profile_picture', 'phone_number']
    success_url = reverse_lazy('profile-page')
    template_name = 'user_signup.html'


#Will need to create template page for succesful deletion or redir to homepage
class UserDeleteView(DeleteView):
    model = UserProfile
    success_url = reverse_lazy('profile-deleted')
    template_name = 'user_profile_delete.html'

# #Views Using Django auth

class UserLoginView(LoginView):
    success_url = reverse_lazy('home-page')
    template_name = 'user_login.html'

class UserLogoutView(LogoutView):
    success_url = reverse_lazy('home-page')
    template_name = 'user_logout.html'

# class UserChangePassword(PasswordChangeView):
#     template_name = 'user_profilePage.html'

# class UserPasswordChangeDone(PasswordChangeDoneView):
#     template_name = 'user_profilePage.html'
