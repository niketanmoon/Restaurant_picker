import random
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#function based view
def home(request):
    num = random.randint(0,1000000000000)
    return render(request,'base.html',{'html_var':'context variable','num':num })
