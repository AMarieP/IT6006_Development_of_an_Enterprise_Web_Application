from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, FormView, ListView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import UserProfile
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

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

class UserProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    context_object_name = 'this_user'
    fields = ['profile_picture', 'phone_number']
    template_name = 'app_user/user_profile_page.html'

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    fields = ['profile_picture', 'phone_number']
    template_name = 'app_user/user_profile_edit.html'
    #Redirects back to User's pfp
    def get_success_url(self, **kwargs):
        return reverse_lazy("profile-page", kwargs={'pk': self.object.pk})

#Succesful deletion redir to homepage
class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    context_object_name = 'this_user'
    success_url = reverse_lazy('home-page')
    template_name = 'app_user/user_profile_delete.html'

#Have to set up but will give a sucessfully deleted message
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(UserDeleteView,self).form_valid(form)

# #Views Using Django auth

class UserLoginView(LoginView):
    redirect_authenticated_user = True
    success_url = reverse_lazy('home-page')
    template_name = 'app_user/user_login.html'
    
    #Error Message, rerender login form
    def form_invalid(self, form):
        print('Invalid')
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

class UserLogoutView(LogoutView):
    success_url = reverse_lazy('home-page')
    template_name = 'app_user/user_logout.html'

# class UserChangePassword(PasswordChangeView):
#     template_name = 'user_profilePage.html'

# class UserPasswordChangeDone(PasswordChangeDoneView):
#     template_name = 'user_profilePage.html'
