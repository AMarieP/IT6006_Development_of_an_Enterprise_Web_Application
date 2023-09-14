from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

#Form using default Django Auth class
class UserForm(forms.ModelForm):
	email = forms.EmailField(required=True)
	password1 = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

#Form for Profile Model
class ProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ("profile_picture", "phone_number")




class UserCreateForm():
	pass

class UserUpdateForm():
	pass

