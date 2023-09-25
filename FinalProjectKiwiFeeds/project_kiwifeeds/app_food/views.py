from django.shortcuts import render
from .models import Food
from .forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from .forms import FoodForm
# Create your views here.
#TODO: View Food List View Does Not Exist


def FoodList(request):
    model = Food.objects.all()
    return render(request,'app_food/food_list.html',{"food_list" : model})

class FoodCreateView(CreateView):
    model = Food
    form_class = FoodForm
    template_name = 'app_food/create_food.html'
  
    # success_url = reverse_lazy('restaurant-list')
    def get_success_url(self):
        # Retrieve the restaurant_id from the URL parameters
        restaurant_id = self.kwargs['restaurant_id']
        
        # Construct the success URL with the restaurant_id
        return reverse_lazy('restaurant-details', kwargs={'restaurant_id': restaurant_id})





# class FoodUpdateView(UpdateView):
#     model = Food
#     form_class = FoodForm
#     template_name = 'app_food/edit_food.html'
    
#     def get_success_url(self):
#         food_id = self.kwargs['food_id']
#         return reverse_lazy('view-food', kwargs={'food_id': food_id})


def EditFood(request,food_id):
    model = Food.objects.get(pk=food_id)
    form = FoodForm()
    if request.method == "POST":
        print(request.POST)
        form=FoodForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
        else:
            form=FoodForm()
        # return HttpResponseRedirect("/food/")
        # for editing food within restaurant page
        return HttpResponseRedirect(f"/restaurants/{model.restaurant.id}/")
    else:
        form=FoodForm(instance=model)

    return render(request,'app_food/edit_food.html',{'form':form})


def DeleteFood(request,food_id):
    model = Food.objects.get(pk=food_id)
    obj = get_object_or_404(Food,id = food_id)

    if request.method == "POST":
        obj.delete()
        # return HttpResponseRedirect("/food/")
        # for editing food within restaurant page
        return HttpResponseRedirect(f"/restaurants/{model.restaurant.id}/")
    return render(request,'app_food/delete_food.html',{'food':model})



