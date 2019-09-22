from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView,View
# Create your views here.

from menus.models import Item
from menus.forms import ItemForm

class HomeView(View):
    def get(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return render(request,'home.html',{})
        user = request.user
        is_following_user_ids = [x.user.id for x in user.is_following.all()]
        qs = Item.objects.filter(user__id__in=is_following_user_ids,public=True).order_by("-updated")[:3]
        return render(request,'menus/home-feed.html',{'object_list':qs})

class ItemListView(LoginRequiredMixin,ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemDetailView(LoginRequiredMixin,DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemCreateView(LoginRequiredMixin,CreateView):
    form_class = ItemForm
    template_name = 'form.html'
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(ItemCreateView,self).get_form_kwargs()
        kwargs['user']= self.request.user
        return kwargs

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ItemCreateView,self).form_valid(form)

    def get_context_data(self,*args,**kwargs):
        context = super(ItemCreateView,self).get_context_data(*args,**kwargs)
        context['title']='Create Item'
        return context

class ItemUpdateView(LoginRequiredMixin,UpdateView):
    form_class = ItemForm
    template_name = 'menus/detail-update.html'
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ItemUpdateView,self).form_valid(form)

    def get_context_data(self,*args,**kwargs):
        context = super(ItemUpdateView,self).get_context_data(*args,**kwargs)
        context['title']='Update Item'
        return context

    def get_form_kwargs(self):
        kwargs = super(ItemUpdateView,self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
