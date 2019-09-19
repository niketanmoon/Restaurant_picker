from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
# Create your views here.

from menus.models import Item
from menus.forms import ItemForm

class ItemListView(ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemDetailView(DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemCreateView(CreateView):
    form_class = ItemForm
    template_name = 'form.html'
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ItemCreateView,self).form_valid(form)

    def get_context_data(self,*args,**kwargs):
        context = super(ItemCreateView,self).get_context_data(*args,**kwargs)
        context['title']='Create Item'
        return context

class ItemUpdateView(UpdateView):
    form_class = ItemForm
    template_name = 'form.html'
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
