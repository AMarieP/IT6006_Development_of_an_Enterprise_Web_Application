from django.contrib import admin
from .models import *

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
  list_display = ("this_user", "profile_picture", "phone_number", "pk")

admin.site.register(UserProfile, UserProfileAdmin)
