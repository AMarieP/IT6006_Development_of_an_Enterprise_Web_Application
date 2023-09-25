from django.shortcuts import get_object_or_404 ,render
from django.views.generic import CreateView,DetailView,ListView,UpdateView
from .models import Review
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from app_reviews.forms import ReviewForm
# Create your views here.
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from app_restaurants.models import Restaurant


# class CreateReview(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
from django.shortcuts import get_object_or_404

class CreateReview(LoginRequiredMixin, CreateView):
    model = Review
    template_name = "app_reviews/create_review.html"
    form_class = ReviewForm
    raise_exception = True

    def handle_no_permission(self):
        # Display a message to the user
        messages.warning(self.request, "You don't have permission to create a review.")
        print('no Permission to add review')
        # Redirect the user to the home page or any other desired URL
        return redirect('home-page')  # Replace 'home' with the URL name of your home page
    
    def get_initial(self):
        # Get the restaurant instance based on the URL parameter
        restaurant_id = self.kwargs['restaurant_id']
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

        # Set initial values for user and restaurant fields
        initial = super().get_initial()
        initial['user'] = self.request.user.userprofile  # Assuming user's profile is stored in 'UserProfile' field
        initial['restaurant'] = restaurant
        print(initial['user'])
        print(initial['restaurant'] )
        return initial

    def form_valid(self, form):
        # Save the form and handle success
        response = super().form_valid(form)
        messages.success(self.request, "Review submitted successfully.")
        return response
    
    def get_success_url(self):
        # Use reverse_lazy with arguments to generate the success URL
        restaurant_id = self.kwargs['restaurant_id']
        return reverse_lazy('restaurant-details', args=[self.kwargs['restaurant_id']])
    

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

