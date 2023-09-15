from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('filter/', views.FilterProductsByTag.as_view(), name='filter'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product'), 
]
