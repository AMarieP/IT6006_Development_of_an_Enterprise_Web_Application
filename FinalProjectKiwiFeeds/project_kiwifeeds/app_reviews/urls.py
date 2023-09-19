from django.urls import path
from .views import CreateReview, ReviewDetail, ReviewList, EditReview

urlpatterns = [
    path("write-a-review/", CreateReview.as_view()),
    path("review/", ReviewDetail.as_view()),
    path("reviews/", ReviewList.as_view()),
    path("edit-review/", EditReview.as_view()),

]