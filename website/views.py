from django.shortcuts import render
from .models import *
from django.views.generic import ListView

# Create your views here.


class HomeView(ListView):
    model = Pages
    template_name = 'home.html'