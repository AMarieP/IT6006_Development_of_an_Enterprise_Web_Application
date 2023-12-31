from django.shortcuts import get_object_or_404 ,render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from app_restaurants.models import Restaurant
from app_restaurants.forms import RestaurantForm
from app_food.forms import FoodForm
from app_favorites.models import Favorites
from app_reviews.models import Review
from django.db.models import Avg

def restaurant_list(request):
    model = Restaurant.objects.all()
    return render(request,'app_restaurants/restaurant_list.html',{"restaurant_list" : model})

def restaurant_details(request, restaurant_id):
    # model = Restaurant.objects.get(pk=restaurant_id)

    # Retrieve the restaurant object or return a 404 error if it doesn't exist
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    # Retrieve the associated reviews for the restaurant
    reviews = restaurant.reviews.all()
     # Calculate the overall rating using Avg
    overall_rating = Review.objects.filter(restaurant=restaurant).aggregate(Avg('rating'))['rating__avg']
    foods=restaurant.food.all()
    # print(reviews)
    # print(foods)
    is_favorite = False

    if request.user.is_authenticated:
        user_profile = request.user.userprofile
        # Check if the restaurant is in the user's favorites
        is_favorite = Favorites.objects.filter(user=user_profile, restaurant=restaurant).exists()
    # print('fav-restaurant')
    # print(is_favorite)
    context = {
        "restaurant": restaurant,
        "reviews": reviews,  # Pass the reviews queryset to the context
         'is_favorite': is_favorite,
         'overall_rating': overall_rating,
         'foods':foods
    }

    return render(request, 'app_restaurants/restaurant_details.html', context)

def RestaurantCreateView(request):
    form=RestaurantForm()
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            # Set the restaurant owner field to the currently logged-in user
            form.instance.restaurant_owner = request.user.userprofile  # Assuming user's profile is stored in 'UserProfile' field

            form.save()
            return HttpResponseRedirect("/restaurants/")
    else:
        # If the request method is not POST, create an empty form with the initial owner
        form = RestaurantForm(initial={'restaurant_owner': request.user.userprofile})  # Assuming user's profile is stored in 'UserProfile' field

    return render(request,'app_restaurants/create_restaurant.html', {"form": form})

# def RestaurantEditView(request, restaurant_id):
#     model = Restaurant.objects.get(pk=restaurant_id)
#     form = RestaurantForm()
#     if request.method =='POST':
#         print(request.POST)
#         form = RestaurantForm(request.POST,instance=model)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/restaurants/")
#         else:
#             form = RestaurantForm()
#     else:
#         form = RestaurantForm(instance=model)

#     return render(request,'app_restaurants/edit_restaurant.html', {"form": form})


def RestaurantEditView(request, restaurant_id):
    # Retrieve the restaurant instance
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    
    
    if request.method == 'POST':
        # Check if the form for editing restaurant details is submitted
        if 'edit_restaurant_form' in request.POST:
            restaurant_form = RestaurantForm(request.POST, instance=restaurant)
            if restaurant_form.is_valid():
                restaurant_form.save()
                return HttpResponseRedirect(f"/restaurants/{restaurant.id}")

    else:
        # Initialize forms for editing restaurant and adding food items
        restaurant_form = RestaurantForm(instance=restaurant)
        # food_form = FoodForm()
    context={
         "restaurant_form": restaurant_form,
        # "food_form": food_form,
        "restaurant": restaurant,
    }
    return render(request, 'app_restaurants/edit_restaurant.html', context)

def RestaurantDeleteView(request, restaurant_id):
    model = {}
    obj = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method =='POST':
        obj.delete()
        return HttpResponseRedirect(reverse('restaurant-list'))
    return render(request,'app_restaurants/delete_restaurant.html', {})
