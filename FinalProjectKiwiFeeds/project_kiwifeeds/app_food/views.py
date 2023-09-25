from django.shortcuts import render
from .models import Food
from .forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from app_restaurants.models import Restaurant
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
    raise_exception = True
    def get_initial(self):
        # Get the restaurant instance based on the URL parameter
        restaurant_id = self.kwargs['restaurant_id']
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

        # Set initial values for user and restaurant fields
        initial = super().get_initial()
        # initial['user'] = self.request.user.userprofile  # Assuming user's profile is stored in 'UserProfile' field
        initial['restaurant'] = restaurant
        # print(initial['user'])
        print(initial['restaurant'] )
        return initial
    # success_url = reverse_lazy('restaurant-list')
    
    def form_valid(self, form):
        # Save the form and handle success
        response = super().form_valid(form)
        messages.success(self.request, "Review submitted successfully.")
        return response
    def get_success_url(self):
        # Use reverse_lazy with arguments to generate the success URL
        restaurant_id = self.kwargs['restaurant_id']
        return reverse_lazy('restaurant-details', args=[self.kwargs['restaurant_id']])
    


class FoodUpdateView(UpdateView):
    model = Food
    form_class = FoodForm
    template_name = 'app_food/edit_food.html'
    raise_exception = True

    def get_object(self, queryset=None):
        # Get the food instance based on the URL parameter
        food_id = self.kwargs['food_id']
        return get_object_or_404(Food, pk=food_id)

    def form_valid(self, form):
        # Save the form and handle success
        response = super().form_valid(form)
     
        print('Food item updated successfully.')
        messages.success(self.request, "Food item updated successfully.")
        return response

    def get_success_url(self):
        # Use reverse_lazy with arguments to generate the success URL
        food_id = self.kwargs['food_id']
        food=Food.objects.get(pk=food_id)
        restaurant_id=food.restaurant.id
        return reverse_lazy('restaurant-details', args=[restaurant_id])


def EditFood(request,food_id):
    model = Food.objects.get(pk=food_id)
    form = FoodForm()
    if request.method == "POST":
        print('request for edit food rcd')
        print(request.POST)
        form=FoodForm(request.POST, instance=model)
        if form.is_valid():
            print('form saved')
            form.save()
        else:
            print('form not valid')
            form=FoodForm()
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



