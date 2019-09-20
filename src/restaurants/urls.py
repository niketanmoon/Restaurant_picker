from django.urls import path

from restaurants.views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView,
    RestaurantUpdateView,
)


app_name='restaurants'
urlpatterns = [
    path('',RestaurantListView.as_view(),name='list'),
    path('create/',RestaurantCreateView.as_view(),name="create"),
    path('<slug>/',RestaurantDetailView.as_view(),name='detail'),
    #path('<slug>/',RestaurantUpdateView.as_view(),name='edit'),
]
