from django.shortcuts import render
from django.http import HttpResponse

from app_restaurants.models import Restaurant
from app_restaurants.forms import RestaurantForm

# Create your views here.
# def review_list(request):
#     model=Review.objects.all()
#     return render(request,'app_restaurants/review_list.html',{"review_list" : model})
# def review_details(request, review_id):
#     model=Review.objects.get(pk=review_id)
#     return render(request, 'app_restaurants/review_details.html',{"review": model})

def restaurant_list(request):
    model=Restaurant.objects.all()
    return render(request,'app_restaurants/restaurant_list.html',{"restaurant_list" : model})
def restaurant_details(request, restaurant_id):
    model=Restaurant.objects.get(pk=restaurant_id)
    return render(request, 'app_restaurants/restaurant_details.html',{"restaurant": model})
def RestaurantCreateView(request):
    form=RestaurantForm()
    return render(request,'app_restaurants/create_restaurant.html', {"form": form})
def RestaurantEditView(request, restaurant_id):
    model = Restaurant.objects.get(pk=restaurant_id)
    form=RestaurantForm()
    if request.method =='POST':
        print(request.Post)
        form=RestaurantForm(request.post,instance=model)
        if form.is_valid():
            form.save()
        else:
            form=RestaurantForm()
    else:
        form=RestaurantForm(instance=model)
    return render(request,'app_restaurants/edit_restaurant.html', {"form": form})
