from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView

from restaurants.forms import RestaurantLocationCreateForm
from restaurants.models import RestaurantLocation
# Create your views here.

@login_required()
def restaurant_createview(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        if request.user.is_authenticated:
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return HttpResponseRedirect("/restaurants/")
        else:
            return HttpResponseRedirect("/login/")
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
