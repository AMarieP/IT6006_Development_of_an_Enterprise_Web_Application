from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def review_list(request):
    return HttpResponse("Hello Reviews")
    #return render(request,'app_review/index.html',{})