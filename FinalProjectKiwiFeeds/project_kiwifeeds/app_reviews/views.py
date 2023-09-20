from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView,UpdateView
from .models import Review
# Create your views here.

class CreateReview(CreateView):
    model = Review
    template_name ="app_reviews/reviews_createreview.html"

class ReviewDetail(DetailView):
    model = Review
    template_name ="app_reviews/reviews_editreview.html"

class ReviewList(ListView):
    model = Review
    template_name = "app_reviews/reviews_reviewdetail.html"

class EditReview(UpdateView):  
    model = Review
    template_name =  "app_reviews/reviews_reviewlist.html"
