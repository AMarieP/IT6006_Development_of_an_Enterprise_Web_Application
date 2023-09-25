# forms.py
from django.forms import ModelForm
from django import forms
    

from .models import Favorites
        
class FavoriteForm(forms.Form):

    restaurant_id = forms.IntegerField(widget=forms.HiddenInput())
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['restaurant_id'].widget = forms.HiddenInput()
        