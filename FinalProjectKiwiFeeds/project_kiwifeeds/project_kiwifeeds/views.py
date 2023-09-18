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
    return render(request, 'restaraunt-catalog.html')