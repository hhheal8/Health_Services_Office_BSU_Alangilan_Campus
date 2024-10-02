from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task



def home(request):
    return render(request,'home.html')    