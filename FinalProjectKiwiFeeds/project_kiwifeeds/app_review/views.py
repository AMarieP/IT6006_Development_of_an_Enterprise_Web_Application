from django.shortcuts import render
from django.http import HttpResponse

from app_review.models import Review

# Create your views here.
def review_list(request):
    model=Review.objects.all()
    return render(request,'app_review/review_list.html',{"review_list" : model})
def review_details(request, review_id):
    return HttpResponse("Review Details")
    #model=Tour.objects.get(pk=tour_id)
    #return render(request, 'tours/tourdetails.html',{"tour": model})