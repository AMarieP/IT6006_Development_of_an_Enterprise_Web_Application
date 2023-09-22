from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
import os

def generate_image_path(instance,filename):
        user_id = instance.id
        # Construct the upload path: 'profile_pics/user_id/filename'
        return os.path.join('profile_pics', str(user_id), 'profile_picture.jpg')

class UserProfile(models.Model):
    # user will be protected if we delete user profile
    this_user = models.OneToOneField(User, on_delete=models.PROTECT)
    profile_picture = models.ImageField(
        default='/profile_pics/temp_pfp_placeholder_REPLACE_LATER.avif',
        upload_to=generate_image_path,  
        height_field=None,
        width_field=None
    )
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=1000)
    #Address model

    def __str__(self):
        return self.this_user.username
    
    def get_absolute_url(self):
        return reverse('profile-page', kwargs={'pk': self.pk})