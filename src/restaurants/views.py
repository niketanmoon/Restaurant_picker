import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from restaurants.models import RestaurantLocation
# Create your views here.
def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset      = RestaurantLocation.objects.all()  #It will create a object list 
    context = {
        "object_list":queryset,
    }
    return render(request,template_name,context)
