from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

# Create your views here.


class HomeView(ListView):
    model = Pages
    template_name = 'home.html'
    context_object_name = 'Pages'

class BlogListView(ListView):
    model = Blogs
    template_name = 'website/bloglist.html'
    context_object_name = 'blogs'
    slug_field = 'slug'
    ordering = ['-id']
    paginate_by = 20

class BlogDetailView(DetailView):
    model = Blogs
    template_name = 'website/blogdetail.html'
    context_object_name = 'blogs'
    slug_field = 'slug'