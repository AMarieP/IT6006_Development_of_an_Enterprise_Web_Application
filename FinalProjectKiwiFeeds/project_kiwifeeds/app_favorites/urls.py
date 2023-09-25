from django.urls import path
from . import views

 # Set the namespace for your app
urlpatterns = [
    # path('add_favorite/<int:restaurant_id>/', views.add_favorite, name='add_favorite'),
    # path('remove_favorite/<int:restaurant_id>/', views.remove_favorite, name='remove_favorite'),
    path('', views.display_favorites, name='my_favorites'),
    path('add-to-favorites/', views.add_to_favorites, name='add-to-favorites'),
    path('remove-from-favorites/<int:restaurant_id>/', views.remove_from_favorites, name='remove-from-favorites'),
]

# the below two lines of code can be used as buttons for adding and removing restaurants from a users list.
#<a href="{% url 'add_favorite' restaurant.id %}">Add to Favorites</a>
#<a href="{% url 'remove_favorite' restaurant.id %}">Remove from Favorites</a>