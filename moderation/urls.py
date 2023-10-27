from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('account/support', views.SupportView.as_view(), name='support')
]