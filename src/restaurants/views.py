import random
from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView,ListView,DetailView

from restaurants.forms import RestaurantCreateForm
from restaurants.models import RestaurantLocation
# Create your views here.

def restaurant_createview(request):
    form = RestaurantCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        obj = RestaurantLocation.objects.create(
                name = form.cleaned_data.get("name"),
                location = form.cleaned_data.get("location"),
                category = form.cleaned_data.get("category")
            )
        return HttpResponseRedirect("/restaurants/")
    if form.errors:
        errors = form.errors

    template_name = 'restaurants/form.html'
    context = {
        "form":form,
        "errors":errors,
    }
    return render(request,template_name,context)

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
