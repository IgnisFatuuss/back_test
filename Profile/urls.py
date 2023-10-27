from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('account/profile/', login_required(views.AccountProfileView.as_view()), name='account-profile'),
    path('account/editprofile/', login_required(views.EditeProfile.as_view()), name='edit-profile'),
    path('account/editaddressview/<slug:slug>/', login_required(views.EditAddressView.as_view()), name='edit-address-view'),
    path('account/editaddressview/', login_required(views.EditAddressView.as_view()), name='edit-address-view'),
    path('account/editaddress/', login_required(views.EditAddress.as_view()), name='edit-address'),
    path('account/addressview/', login_required(views.AddressView.as_view()), name='addresses-view'),
    path('account/removeaddress/<slug:slug>/', login_required(views.RemoveAddress.as_view()), name='remove-address'), 
    path('account/makedefault/<slug:slug>/', login_required(views.MakeDefalut.as_view()), name='make-defalut'),
    path('account/dashboard', login_required(views.DashboardView.as_view()), name='dashboard'),
    path('account/orders', login_required(views.OrdersView.as_view()), name='orders-view'),
    path('account/order-details/<slug:slug>/', login_required(views.OrderDetails.as_view()), name='order-details'), 
    path('account/reviews-history', login_required(views.ReviewsView.as_view()), name='reviews-history'),
    path('account/edit-review/<str:id>', login_required(views.ReviewEditView.as_view()), name='edit-review'),
    path('account/faq-history', login_required(views.FaqView.as_view()), name='faq-history'),
    path('account/claim/<str:id>', login_required(views.MakeClaim.as_view()), name='make-claim'),
    path('account/claims', login_required(views.ClaimsView.as_view()), name='claims'),
]


# urlpatterns = [
#     path('account/profile/', views.AccountProfileView.as_view(), name='account-profile'),
#     path('account/editprofile/', views.EditeProfile.as_view(), name='edit-profile'),
#     path('account/editaddressview/<slug:slug>/', views.EditAddressView.as_view(), name='edit-address-view'),
#     path('account/editaddressview/', views.EditAddressView.as_view(), name='edit-address-view'),
#     path('account/editaddress/', views.EditAddress.as_view(), name='edit-address'),
#     path('account/addressview/', views.AddressView.as_view(), name='addresses-view'),
#     path('account/removeaddress/<slug:slug>/', views.RemoveAddress.as_view(), name='remove-address'), 
#     path('account/makedefault/<slug:slug>/', views.MakeDefalut.as_view(), name='make-defalut'),
#     path('account/dashboard', views.DashboardView.as_view(), name='dashboard'),
#     path('account/orders', views.OrdersView.as_view(), name='orders-view'),
#     path('account/order-details/<slug:slug>/', views.OrderDetails.as_view(), name='order-details'), 
#     path('account/reviews-history', views.ReviewsView.as_view(), name='reviews-history'),
# ]