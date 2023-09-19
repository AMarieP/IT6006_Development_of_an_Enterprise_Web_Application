from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# def home(request):
    
#     return render(request,'index.html')
#     # return HttpResponse("Hello, World!")


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')

def restaraunt_catalog(request):
    context={
        'r_name':"Hoppers",
        'r_address':"134b Ponsonby Road, Grey Lynn, Auckland 1011",
        'r_rating':80,
        'r_desc':"Overnight grew a magical world from scratch, inviting all walks of life to experience, taste and observe weird and delightful things in its Peculiar Garden. Revealing 18 Craft Beer taps, fine wines, botanical gin cocktails and an exciting array of sharing plates, Hoppers was created solely with the adventurous in mind.",
    }
    return render(request, 'restaraunt-catalog.html', context)

def login_or_signup(request):
    return render(request, "login-or-signup.html")

def restaraunt_details(request):
    context={
        'r_name':"Hoppers",
        'r_address':"134b Ponsonby Road, Grey Lynn, Auckland 1011",
        'r_rating':80,
        'r_desc':"Overnight grew a magical world from scratch, inviting all walks of life to experience, taste and observe weird and delightful things in its Peculiar Garden. Revealing 18 Craft Beer taps, fine wines, botanical gin cocktails and an exciting array of sharing plates, Hoppers was created solely with the adventurous in mind.",
    }
    return render(request, 'restaurant-details.html', context)
