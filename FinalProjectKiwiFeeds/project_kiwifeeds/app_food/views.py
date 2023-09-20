from django.shortcuts import render
from .models import Food
from .forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your views here.
#TODO: View Food List View Does Not Exist


def CreateFood(request):
    form=FoodForm()
    if request.method == "POST":
        print(request.POST)
        form=FoodForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'app_food/create_food.html',{'form':form})


def EditFood(request,Food_id):
    model = Food.objects.get(pk=Food_id)
    form = FoodForm()
    if request.method == "POST":
        print(request.POST)
        form=FoodForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
        else:
            form=FoodForm()
    else:
        form=FoodForm(instance=model)
    return render(request,'app_food/edit_food.html',{'form':form})


def DeleteFood(request,Food_id):
    model = Food
    obj = get_object_or_404(Food,id = Food_id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect('food')
    return render(request,'app_food/delete_food.html',{'food':model})



