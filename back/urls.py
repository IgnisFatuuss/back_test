from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('_nested_admin/', include('nested_admin.urls')),
    path("admin/", admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('website.urls')),
    path('', include('shops.urls')),
    path('', include('Profile.urls')),
    path('pages', include('django.contrib.flatpages.urls')),
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('registration/', views.RegistrationView.as_view(), name='register'),
    # path('account/', views.EditProfileView.as_view(), name='edit_profile'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)