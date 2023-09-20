from django.forms import ModelForm
from .models import Restaurant

class RestaurantForm(ModelForm):

    class Meta:
        model = Restaurant
        fields = ["restaurant_name","restaurant_owner","restaurant_description","restaurant_location"]
