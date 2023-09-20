from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    this_user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='/profile_pics/temp_pfp_placeholder_REPLACE_LATER.avif', upload_to='profile_pics', height_field=None, width_field=None)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=1000)
    #Address model

    def __str__(self):
        return self.this_user.username
    
    def get_absolute_url(self):
        return reverse('profile-page', kwargs={'pk': self.pk})