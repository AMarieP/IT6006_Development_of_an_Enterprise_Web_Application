from django.shortcuts import render
from django.http import HttpResponse

from app_review.models import Restaurant, Review

# Create your views here.
def review_list(request):
    model=Review.objects.all()
    return render(request,'app_review/review_list.html',{"review_list" : model})
def review_details(request, review_id):
    model=Review.objects.get(pk=review_id)
    return render(request, 'app_review/review_details.html',{"review": model})
def restaurant_list(request):
    model=Restaurant.objects.all()
    return render(request,'app_review/restaurant_list.html',{"restaurant_list" : model})