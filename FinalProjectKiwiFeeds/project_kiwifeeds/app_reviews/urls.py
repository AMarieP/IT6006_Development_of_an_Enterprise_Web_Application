from django.urls import path
from .views import CreateReview, ReviewDetail, ReviewList, EditReview

urlpatterns = [
    path("write-a-review/", CreateReview.as_view(), name='write-a-review'),
    path("<int:pk>/review/", ReviewDetail.as_view(), name='review'),
    path("reviews/", ReviewList.as_view(), name='review-list'),
    path("/<int:pk>/edit-review/", EditReview.as_view(), name='edit-review'),

]