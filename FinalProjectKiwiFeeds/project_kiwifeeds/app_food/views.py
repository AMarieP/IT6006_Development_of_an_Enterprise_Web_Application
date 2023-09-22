from django.shortcuts import render
from .models import Food
from .forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
#TODO: View Food List View Does Not Exist

def FoodList(request):
    model = Food.objects.all()
    return render(request,'app_food/food_list.html',{"food_list" : model})


def CreateFood(request):
    form=FoodForm()
    if request.method == "POST":
        print(request.POST)
        form=FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/food/")
    return render(request,'app_food/create_food.html',{'form':form})


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
        return HttpResponseRedirect(f"/restaurants/{model.restaurant.id}/edit/")
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
        return HttpResponseRedirect(f"/restaurants/{model.restaurant.id}/edit/")
    return render(request,'app_food/delete_food.html',{'food':model})



