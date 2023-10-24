from django.urls import path
from . import views
from .views import get_price_variations



urlpatterns = [
    path('search/', views.SearchView.as_view(), name='search'),
    path('', views.ProductListView.as_view(), name='index'),
    # path('shopfilter/',  views.ShopFilter.as_view(), name='shopfilter'),
    path('filter/', views.FilterProductsByTag.as_view(), name='filter'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product'), 
    path('shop/', views.ProductShop.as_view(), name='shop'),
    path('search/', views.ProductSearch.as_view(), name='search'),
    path('get_price_variations/', get_price_variations , name='get_price_variations'),
    path('categories/<slug:slug>/', views.CategoriesShops.as_view() , name='categories'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('add-to-cart/<str:slug>', views.AddToCartView.as_view(), name='add-to-cart'),
    path('change-qty/<str:slug>', views.ChangeQTY.as_view(), name='change-qty'),
    path('deleteproductfromcart/<str:slug>', views.DeleteProductFromCart.as_view(), name='delete-product'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('makeorder/', views.MakeOrderView.as_view(), name='make-order'),
    path('makereview/', views.MakeReview.as_view(), name='make-review'),
    path('makerequestion/', views.MakeQuestion.as_view(), name='make-question'),
    path('makeansnwer/', views.MakeAnswer.as_view(), name='make-answer'),
    path('wishlist/', views.WishListView.as_view(), name='wishlist'),
    path('add-to-wishlist/<str:slug>', views.AddToWishList.as_view(), name='add-to-wishlist'),
    path('remove-from-wishlist/<str:slug>', views.RemoveFromWishList.as_view(), name='remove-from-wishlist'),
    path('stores/', views.StoresListView.as_view(), name='stores'),
    path('store/<slug:slug>/', views.StoreDetailView.as_view(), name='store'), 
    path('store/about/<slug:slug>/', views.StoreAboutView.as_view(), name='storeabout'), 
]
