from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView,UpdateView
from .models import Review
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from app_reviews.forms import ReviewForm
# Create your views here.
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect

class CreateReview(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Review
    template_name ="app_reviews/create_review.html"
    success_url = reverse_lazy('review-list')
    form_class = ReviewForm
    permission_required = 'app_reviews.add_review'
    raise_exception = True
    
    def handle_no_permission(self):
        # Display a message to the user
        messages.warning(self.request, "You don't have permission to create a review.")
        
        # Redirect the user to the home page or any other desired URL
        return redirect('home-page')  # Replace 'home' with the URL name of your home page


class ReviewList(ListView):
    model = Review
    template_name = "app_reviews/reviews_list.html"
    context_object_name = 'reviews'
   
class EditReviewView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = Review
    fields = ['restaurant', 'user', 'rating', 'review']
    template_name = 'app_reviews/edit_review.html'
    success_url = '/reviews/' 
    permission_required = 'app_reviews.add_review'
    raise_exception = True
    
#These views are not in current app scope
# class ReviewDetail(DetailView):
#     model = Review
#     template_name ="app_reviews/reviews_editreview.html"

# class EditReview(LoginRequiredMixin, UpdateView):  
#     model = Review
#     template_name =  "app_reviews/reviews_reviewlist.html"
#     def get_success_url(self, **kwargs):
#         return reverse_lazy("review", kwargs={'pk': self.object.pk})

