import random
from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView,DetailView

from restaurants.models import RestaurantLocation
# Create your views here.

class RestaurantListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__icontains = slug) |
                Q(category__iexact = slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset

class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()
    def get_object(self,*args,**kwargs):
        rest_id = self.kwargs.get("rest_id")
        obj = get_object_or_404(RestaurantLocation, pk=rest_id)
        return obj
