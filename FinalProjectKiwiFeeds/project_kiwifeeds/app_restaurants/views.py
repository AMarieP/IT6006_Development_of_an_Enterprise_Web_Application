from django.shortcuts import get_object_or_404 ,render
from django.http import HttpResponse, HttpResponseRedirect

from app_restaurants.models import Restaurant
from app_restaurants.forms import RestaurantForm

def restaurant_list(request):
    model=Restaurant.objects.all()
    return render(request,'app_restaurants/restaurant_list.html',{"restaurant_list" : model})
def restaurant_details(request, restaurant_id):
    model=Restaurant.objects.get(pk=restaurant_id)
    return render(request, 'app_restaurants/restaurant_details.html',{"restaurant": model})
def RestaurantCreateView(request):
    form=RestaurantForm()
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'app_restaurants/create_restaurant.html', {"form": form})
def RestaurantEditView(request, restaurant_id):
    model = Restaurant.objects.get(pk=restaurant_id)
    form=RestaurantForm()
    if request.method =='POST':
        print(request.POST)
        form=RestaurantForm(request.POST,instance=model)
        if form.is_valid():
            form.save()
        else:
            form=RestaurantForm()
    else:
        form=RestaurantForm(instance=model)
    return render(request,'app_restaurants/edit_restaurant.html', {"form": form})
def RestaurantDeleteView(request, restaurant_id):
    model={}
    obj = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method =='POST':
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request,'app_restaurants/delete_restaurant.html', {})
