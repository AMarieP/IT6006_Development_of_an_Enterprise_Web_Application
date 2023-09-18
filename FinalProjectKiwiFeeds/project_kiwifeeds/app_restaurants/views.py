from django.shortcuts import render
from django.http import HttpResponse

from app_restaurants.models import Restaurant

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