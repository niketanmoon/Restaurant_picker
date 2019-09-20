from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView

from restaurants.forms import RestaurantLocationCreateForm
from restaurants.models import RestaurantLocation
# Create your views here.

class RestaurantListView(LoginRequiredMixin,ListView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantCreateView(LoginRequiredMixin,CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = "form.html"
    #success_url = '/restaurants/'

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView,self).form_valid(form)

    def get_context_data(self,*args,**kwargs):
        context = super(RestaurantCreateView,self).get_context_data(*args,**kwargs)
        context['title'] = 'Add Restaurant'
        return context

class RestaurantUpdateView(LoginRequiredMixin,UpdateView):
    form_class = RestaurantLocationCreateForm
    template_name = "restaurants/detail-update.html"

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

    def get_context_data(self,*args,**kwargs):
        context = super(RestaurantUpdateView,self).get_context_data(*args,**kwargs)
        name = self.get_object().name
        context['title'] = f'Update Restaurant: {name}'
        return context
