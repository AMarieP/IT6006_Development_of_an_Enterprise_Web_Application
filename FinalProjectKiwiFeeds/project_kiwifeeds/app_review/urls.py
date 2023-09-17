from django.urls import path
from views import review_list

urlpatterns = [
   path("",review_list ,name="home"),
   path("reviews/", review_list, name="reviewlist"),
   path("review/<int:review_id>", review_list, name="review-details")

]