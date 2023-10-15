# from django.contrib.auth.mixins import LoginRequiredMixin
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import ListView, DetailView, TemplateView, View
from .models import *
from shops.models import *
from .forms import *
from django.db import transaction
# from .models import Pages, User
# from website.models import GeneralSettings
# from django.contrib.auth import authenticate, login, logout
# from django.views import View
# from .forms import LoginForm, UserProfileForm, RegistrationForm
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from django.contrib import messages
# import time

class AccountProfileView(View):
    def get(self, request, *args, **kwargs):
        context ={
            'profiles': Profile.objects.all(),
            'form' : ProfileForm
        }

        return render(request, 'profiles/account-profile.html', context)
    
class EditeProfile(View):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        p = Profile.objects.get(user = self.request.user)
        if p:
            form = ProfileForm(request.POST or None)
            if form.is_valid():
                for field, value in form.cleaned_data.items():
                    setattr(p, field, value)
                p.save()
                return HttpResponseRedirect('/addressview/')
        else:
            form = ProfileForm(request.POST or None)
            if form.is_valid():
                edited_profile = form.save(commit=False)
                for field, value in form.cleaned_data.items():
                    setattr(edited_profile, field, value)
                edited_profile.user = self.request.user
                edited_profile.save()  # Сохраните объект профиля
                return HttpResponseRedirect('/addressview/')  # Перенаправить пользователя на страницу профиля после успешного сохранения
        
        return HttpResponseRedirect('/addressview/')
    
class EditAddressView(View):
    def get(self, request, *args, **kwargs):
        context ={
            'form' : AdressEditForm
        }
        try:
            request.session['address-slug'] = kwargs['slug']
        except:
            request.session['address-slug'] = None

        return render(request, 'profiles/edit-address.html', context)
    
class EditAddress(View):
    
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        slug = self.request.session.get('address-slug') #id адреса, который нужно изменить. передается лишь в том случае если была нажата кнопка изменения
        if slug == None:
            form = AdressEditForm(request.POST or None)
            if form.is_valid():
                edited_address = form.save(commit=False)
                for field, value in form.cleaned_data.items():
                        setattr(edited_address, field, value)
                edited_address.user = self.request.user
                edited_address.save()  # Сохраните объект профиля
                return HttpResponseRedirect('/addressview/')  # Перенаправить пользователя на страницу профиля после успешного сохранения
        else:
            form = AdressEditForm(request.POST or None)
            if form.is_valid():
                address = Adress.objects.get(id=slug)
                for field, value in form.cleaned_data.items():
                    setattr(address, field, value)
                address.save()
                request.session['address-slug'] = None
                return HttpResponseRedirect('/addressview/')
        
        return HttpResponseRedirect('/addressview/')

class RemoveAddress(View):
    def get(self, request, *args, **kwargs):
        address = Adress.objects.filter(id = kwargs['slug'])
        if address:
            address.delete()
        
        return HttpResponseRedirect('/addressview/')

class AddressView(ListView):
    model = Adress
    template_name = 'profiles/account-addresses.html'
    context_object_name = 'addresses'

class MakeDefalut(View):
    def get(self, request, *args, **kwargs):
        address = Adress.objects.get(id = kwargs['slug'])
        if address:
            address.default = True
            address.save()
        return HttpResponseRedirect('/addressview/')

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        context ={
            'profile' : Profile.objects.get(user = self.request.user),
            'default_address' : Adress.objects.get(default=True),
            'orders' : Orders.objects.all(),
        }

        return render(request, 'profiles/dashboard.html', context)
    
class OrdersView(ListView):
    model = Orders
    template_name = 'profiles/account-orders.html'
    context_object_name = 'orders'
    ordering = ['-id']

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        queryset.filter(user=self.request.user)

        return queryset

class OrderDetails(DetailView):
    model = Orders
    template_name = 'profiles/account-order-details.html'
    context_object_name = 'order'
    slug_field = 'id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Orders.objects.get(id = self.kwargs['slug']).cart
        cartproducts = cart.products.all()
        context['cartproducts'] = cartproducts
        return context

# class EditProfileView(CustomHtmxMixin, TemplateView):
#     template_name = 'profile.html'

#     @method_decorator(login_required)
#     def get(self, request, args, **kwargs):
#         form = UserProfileForm(instance=request.user)
#         context = self.get_context_data(form=form, title='Личные данные')
#         return self.render_to_response(context)

#     @method_decorator(login_required)
#     def post(self, request,args, kwargs):
#         form = UserProfileForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('edit_profile')
#         context = self.get_context_data(form=form, title='Личные данные')
#         return self.render_to_response(context)

#     def get_context_data(self, kwargs):
#         kwargs['title'] = 'Профиль'
#         return super().get_context_data(**kwargs)
# class CustomHtmxMixin:
#     def dispatch(self, request, args, **kwargs):
#         self.template_htmx = self.template_name
#         if not self.request.META.get('HTTP_HX_REQUEST'):
#             self.template_name = 'themes/include_block.html'
#         else:
#             time.sleep(1)
#         return super().dispatch(request,args, kwargs)
#     def get_context_data(self, kwargs):
#         kwargs['template_htmx'] = self.template_htmx
#         return super().get_context_data(**kwargs)
# class LoginView(View):
#     template_name = 'login.html'

#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect(
#                 'edit_profile')  # Если пользователь уже авторизован, перенаправьте его на страницу 'edit_profile'

#         form = LoginForm()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 if user.blocked:
#                     messages.error(request, "Ваш аккаунт заблокирован.")
#                     return redirect('login')
#                 login(request, user)
#                 return redirect('edit_profile')
#         return render(request, self.template_name, {'form': form})

# class RegistrationView(View):
#     template_name = 'register.html'

#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('edit_profile')

#         general_settings = GeneralSettings.objects.first()

#         if general_settings.registration == 1:
#             form = RegistrationForm()
#             return render(request, self.template_name, {'form': form})
#         else:
#             return render(request, self.template_name, {'message': general_settings.of_register_message})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('edit_profile')

#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('edit_profile')
#         return render(request, self.template_name, {'form': form})