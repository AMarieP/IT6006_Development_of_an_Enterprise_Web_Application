from django.shortcuts import render
from django.http import HttpResponse

from app_review.models import Review

# Create your views here.
def review_list(request):
    model=Review.objects.get();
    #return HttpResponse("Hello Reviews")
    return render(request,'app_review/review_list.html',{review_list : model})