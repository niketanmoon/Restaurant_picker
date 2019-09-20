from django.urls import path

from menus.views import (
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView
)


app_name='menus'
urlpatterns = [
    path('',ItemListView.as_view(),name='list'),
    path('create/',ItemCreateView.as_view(),name="create"),
    path('<pk>/',ItemDetailView.as_view(),name='detail'),
    path('<pk>/edit/',ItemUpdateView.as_view(),name='update'),
]
