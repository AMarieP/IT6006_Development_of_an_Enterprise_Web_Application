from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView,UpdateView
from .models import Review
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from app_reviews.forms import ReviewForm
# Create your views here.

class CreateReview(LoginRequiredMixin, CreateView):
    model = Review
    template_name ="app_reviews/create_review.html"
    success_url = reverse_lazy('review-list')
    form_class = ReviewForm


class ReviewList(ListView):
    model = Review
    template_name = "app_reviews/reviews_list.html"
    context_object_name = 'reviews'

class EditReviewView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['restaurant', 'user', 'rating', 'review']
    template_name = 'app_reviews/edit_review.html'
    success_url = '/reviews/' 
    
#These views are not in current app scope
# class ReviewDetail(DetailView):
#     model = Review
#     template_name ="app_reviews/reviews_editreview.html"

# class EditReview(LoginRequiredMixin, UpdateView):  
#     model = Review
#     template_name =  "app_reviews/reviews_reviewlist.html"
#     def get_success_url(self, **kwargs):
#         return reverse_lazy("review", kwargs={'pk': self.object.pk})

