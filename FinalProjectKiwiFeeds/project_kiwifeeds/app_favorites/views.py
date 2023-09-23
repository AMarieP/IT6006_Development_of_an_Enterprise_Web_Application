from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Favorites
from app_restaurants.models import Restaurant
from app_user.models import UserProfile
from django.shortcuts import redirect, render
from .models import Favorites
from app_favorites.forms import FavoriteForm


# @login_required
# def add_favorite(request, restaurant_id):
#     restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    
    
#     if not Favorites.objects.filter(user=request.user, restaurant=restaurant).exists():
#         Favorites.objects.create(user=request.user, restaurant=restaurant)
#     context={

#     }
#     return redirect('restaurant_detail', context)  

# @login_required
# def remove_favorite(request, restaurant_id):
#     restaurant = get_object_or_404(Restaurant, id=restaurant_id)
#     favorite = Favorites.objects.filter(user=request.user, restaurant=restaurant).first()
    
#     if favorite:
#         favorite.delete()
#     context={

#     }
    
#     # return redirect('restaurant_detail', restaurant_id=restaurant_id)  
#     return redirect('restaurant_detail', context)  


def add_to_favorites(request):
    if request.method == 'POST':
        form = FavoriteForm(request.POST)
        if form.is_valid():
            restaurant_id = form.cleaned_data['restaurant_id']
            # Perform the logic to add the restaurant to the user's favorites
            restaurant = get_object_or_404(Restaurant, id=restaurant_id)
            if not Favorites.objects.filter(user=request.user.userprofile, restaurant=restaurant).exists():
                 Favorites.objects.create(user=request.user.userprofile, restaurant=restaurant)
            
            print( 'added to fav ')
    return redirect('restaurant-details', restaurant_id=restaurant_id)

def remove_from_favorites(request, restaurant_id):
    
    print("removing from fav rest list")
    print(restaurant_id)
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    favorite = Favorites.objects.filter(user=request.user.userprofile, restaurant=restaurant).first()
            
    if favorite:
        favorite.delete()
        print('fav rest removed 1')

   
     
    return redirect('restaurant-details', restaurant_id=restaurant_id)


@login_required
def display_favorites(request):
    # first get the current user 
    user_profile = request.user.userprofile
    # with related name get all favorites restaurants from app_Favorite
    fav_restaurants = Favorites.objects.filter(user=user_profile)

    context={
        "user_profile":user_profile,
        'fav_restaurants':fav_restaurants,
    }
    return render(request, 'app_favorites/favorites.html', context)