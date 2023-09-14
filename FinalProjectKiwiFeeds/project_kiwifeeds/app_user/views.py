from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, FormView, ListView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from .models import UserProfile
from .forms import *
from django.http import HttpResponseRedirect

#Create a user, render the default User form as well as the UserPrfile odel on One Page
class UserCreateView(CreateView):

    def get(self, request, *args, **kwargs):
        context = {'user_form': UserForm(), 'profile_form': ProfileForm()}
        return render(request, 'app_user/user_signup.html', context)

    def post(self, request, *args, **kwargs):
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            #save the User
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            #Do not save the profile yet so we can set things as we want
            profile = profile_form.save(commit=False)
            profile.this_user = user #This sets the FK to the user we just saved
            if 'picture' in request.FILES:#sets the pfp
                profile.profile_picture = request.FILES['picture']
            profile.save()
            return HttpResponseRedirect(reverse_lazy('profile-page', kwargs={'pk': profile.pk}))
        else:
            print ('user: ', user_form.errors, 'profile: ', profile_form.errors)

        return render(request, 'app_user/user_signup.html', {'user_form': UserForm(), 'profile_form': ProfileForm()})
    # success_url = reverse_lazy('profile-page')
    # template_name = 'app_user/user_signup.html'

class UserProfileView(DetailView):
    model = UserProfile
    # fields = ['profile_picture', 'phone_number']
    template_name = 'app_user/user_profile_page.html'

class UserUpdateView(UpdateView):
    model = UserProfile
    fields = ['profile_picture', 'phone_number']
    success_url = reverse_lazy('profile-page')
    template_name = 'app_user/user_profile_edit.html'

#Will need to create template page for succesful deletion or redir to homepage
class UserDeleteView(DeleteView):
    model = UserProfile
    success_url = reverse_lazy('profile-deleted')
    template_name = 'app_user/user_profile_delete.html'

# #Views Using Django auth

class UserLoginView(LoginView):
    success_url = reverse_lazy('home-page')
    template_name = 'app_user/user_login.html'

class UserLogoutView(LogoutView):
    success_url = reverse_lazy('home-page')
    template_name = 'app_user/user_logout.html'

# class UserChangePassword(PasswordChangeView):
#     template_name = 'user_profilePage.html'

# class UserPasswordChangeDone(PasswordChangeDoneView):
#     template_name = 'user_profilePage.html'
