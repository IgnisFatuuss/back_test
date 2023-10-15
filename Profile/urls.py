from django.urls import path
from . import views



urlpatterns = [
    path('account-profile/', views.AccountProfileView.as_view(), name='account-profile'),
    path('editprofile/', views.EditeProfile.as_view(), name='edit-profile'),
    path('editaddressview/<slug:slug>/', views.EditAddressView.as_view(), name='edit-address-view'),
    path('editaddressview/', views.EditAddressView.as_view(), name='edit-address-view'),
    path('editaddress/', views.EditAddress.as_view(), name='edit-address'),
    path('addressview/', views.AddressView.as_view(), name='addresses-view'),
    path('removeaddress/<slug:slug>/', views.RemoveAddress.as_view(), name='remove-address'), 
    path('makedefault/<slug:slug>/', views.MakeDefalut.as_view(), name='make-defalut'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('account-orders', views.OrdersView.as_view(), name='orders-view'),
    path('order-details/<slug:slug>/', views.OrderDetails.as_view(), name='order-details'), 
]