from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *
from django.db.models import Prefetch
# Create your views here.

class GetTags:
    def get_tags(self):
        return Tags.objects.all()

class ProductListView(ListView, GetTags):
    model = Products
    template_name = 'shops/productlist.html'
    context_object_name = 'products'
    slug_field = 'slug'
    ordering = ['-id']


    def get_queryset(self):
        return Products.objects.prefetch_related(
            Prefetch('variations__gallereis', queryset=Gallereis.objects.all().order_by('id'))
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Categories.objects.all()
        brands = Brands.objects.all()
        variations = Variations.objects.all()
        product = get_object_or_404(Products, slug=self.kwargs['slug'])
        images = Gallereis.objects.filter(variations__products=product)
        context['categories'] = categories
        context['brands'] = brands
        context['image'] = images
        return context
    
class FilterProductsByTag(GetTags, ListView):
    def get_queryset(self) -> QuerySet[Any]:
        queryset = Products.objects.filter(tag__in = self.request.GET.getlist('slug'))
        return queryset
    
class ProductDetailView(DetailView):
    model = Products
    template_name = 'shops/productdetail.html'
    context_object_name = 'product'
    slug_field = 'slug'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.object.brand  
        tags = self.object.tag.all()
        selected_products = Products.objects.filter(tag__in=tags).exclude(pk=self.object.pk)
        context['brand'] = brand
        context['selected_products'] = selected_products
        context['tags'] = tags
        return context