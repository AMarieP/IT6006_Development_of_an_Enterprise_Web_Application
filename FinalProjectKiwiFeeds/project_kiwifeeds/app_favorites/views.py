from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Favorites
from app_restaurants.models import Restaurant

@login_required
def add_favorite(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    
    
    if not Favorites.objects.filter(user=request.user, restaurant=restaurant).exists():
        Favorites.objects.create(user=request.user, restaurant=restaurant)
    
    return redirect('restaurant_detail', restaurant_id=restaurant_id)  

@login_required
def remove_favorite(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    favorite = Favorites.objects.filter(user=request.user, restaurant=restaurant).first()
    
    if favorite:
        favorite.delete()
    
    return redirect('restaurant_detail', restaurant_id=restaurant_id)  

@login_required
def display_favorites(request):
    user_favorites = Favorites.objects.filter(user=request.user)
    return render(request, 'app_favorites/favorites.html', {'user_favorites': user_favorites})