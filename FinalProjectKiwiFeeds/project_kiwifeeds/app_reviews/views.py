from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView,UpdateView
from .models import Review
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class CreateReview(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['restaurant', 'user', 'rating', 'review']
    template_name ="app_reviews/reviews_createreview.html"
    def get_success_url(self, **kwargs):
        return reverse_lazy("review", kwargs={'pk': self.object.pk})


class ReviewDetail(DetailView):
    model = Review
    template_name ="app_reviews/reviews_editreview.html"

class ReviewList(ListView):
    model = Review
    template_name = "app_reviews/reviews_reviewdetail.html"

class EditReview(LoginRequiredMixin, UpdateView):  
    model = Review
    template_name =  "app_reviews/reviews_reviewlist.html"
    def get_success_url(self, **kwargs):
        return reverse_lazy("review", kwargs={'pk': self.object.pk})

