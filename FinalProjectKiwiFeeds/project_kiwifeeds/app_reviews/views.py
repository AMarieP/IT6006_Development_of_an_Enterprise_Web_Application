from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView,UpdateView
from .models import Review
# Create your views here.

class CreateReview(CreateView):
    model = Review

class ReviewDetail(DetailView):
    model = Review

class ReviewList(ListView):
    model = Review

class EditReview(UpdateView):  
    model = Review

