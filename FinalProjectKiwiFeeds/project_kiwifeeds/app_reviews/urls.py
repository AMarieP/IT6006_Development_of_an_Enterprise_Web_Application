from django.urls import path
from .views import CreateReview, ReviewList,EditReviewView

urlpatterns = [
    path("<int:restaurant_id>/write-a-review/", CreateReview.as_view(), name='write-a-review'),
    path("", ReviewList.as_view(), name='review-list'),
    # path("/<int:pk>/edit-review/", EditReviewView.as_view(), name='edit-review'),

]