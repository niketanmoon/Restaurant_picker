"""picky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from restaurants.views import (
    RestaurantListView,
)



urlpatterns = [
    path('restaurants/',RestaurantListView.as_view()),
    path('restaurants/<slug>/',RestaurantListView.as_view()),
    path('about/',TemplateView.as_view(template_name = "about.html")),
    path('contact/',TemplateView.as_view(template_name = "contact.html")),
    path('admin/', admin.site.urls),
]
