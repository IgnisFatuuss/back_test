from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import ListView, DetailView, View, TemplateView
from .models import *
from django.http import JsonResponse
from django.db.models import Prefetch, Q, Min, Max
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponseRedirect
from .forms import *
from .utils import recalc_cart
from django.db import transaction
# from Profile.models import Adress
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
        queryset = super().get_queryset()
        tag_id = self.request.GET.get('tag_id')  # Получаем значение id тега из GET-параметра
        if tag_id:
            tag = get_object_or_404(Tags, id=tag_id)  # Получаем объект тега по его id
            queryset = queryset.filter(tag=tag).distinct() # Фильтруем продукты по выбранному тегу
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Categories.objects.all()
        brands = Brands.objects.all()
        product_tag_1 = Products.objects.filter(tag__id=2)
        context['slider'] = Sliders.objects.get(id = 1)
        context['banner'] = Banners.objects.get(id = 1)
        context['categories'] = categories
        context['brands'] = brands
        context['product_tag_1'] = product_tag_1
        return context
    
class FilterProductsByTag(GetTags, ListView):
    model = Products
    template_name = 'your_template.html'
    context_object_name = 'products'
    ordering = ['-id']

    def get_queryset(self):
        tag_id = self.request.GET.get('tag_id')
        queryset = super().get_queryset()

        if tag_id:
            queryset = queryset.filter(tag__id=tag_id)

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
        form = ReviewForm(self.request.POST or None)
        questionform = QuestionForm(self.request.POST or None)
        # users = self.request.user.is_staff
        answerform = AnswerForm(self.request.POST or None)
        wishlist = WishList.objects.filter(product=Products.objects.get(slug=self.kwargs['slug']))
        context['wishlist'] = wishlist
        context['questionform'] = questionform
        context['form'] = form
        context['answerform'] = answerform
        context['brand'] = brand
        context['selected_products'] = selected_products
        context['tags'] = tags
        # context['users'] = users
        return context
    
class MakeReview(View):
    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.text = form.cleaned_data['text']
            new_review.review = form.cleaned_data['review']
            # print(self.request.GET.getlist('product-id'))
            product = Products.objects.get(id = self.request.POST.get('product-id'))
            new_review.product = product
            
            new_review.save()
            # print('product/{}'.format(product.slug))
            return HttpResponseRedirect('product/{}'.format(product.slug))
        return HttpResponseRedirect('/product/{}'.format(product.slug))
    
class MakeQuestion(View):
    def post(self, request, *args, **kwargs):
        form = QuestionForm(request.POST or None)
        if form.is_valid():
            new_q = form.save(commit=False)
            new_q.user = request.user
            new_q.question = form.cleaned_data['question']
            product = Products.objects.get(id = self.request.POST.get('product-id'))
            new_q.product = product
            new_q.save()
            return HttpResponseRedirect('/product/{}'.format(product.slug))
        return HttpResponseRedirect('/product/{}'.format(product.slug))

class MakeAnswer(View):
    def post(self, request, *args, **kwargs):
        form = AnswerForm(request.POST or None)
        if form.is_valid():
            # new_q = form.save(commit=False)
            # new_q.user = request.user
            # new_q.question = form.cleaned_data['question']
            # product = Products.objects.get(id = self.request.POST.get('product-id'))
            # new_q.product = product
            # new_q.save()
            product = Products.objects.get(id = self.request.POST.get('product-id'))
            faq = Faqs.objects.get(id = self.request.POST.get('faq-id'))
            faq.answer=form.cleaned_data['answer']
            faq.save()
            return HttpResponseRedirect('/product/{}'.format(product.slug))
        return HttpResponseRedirect('/product/{}'.format(product.slug))

class ProductShop(ListView):
    model = Products
    template_name = 'shops/shop.html'
    context_object_name = 'products'
    slug_field = 'slug'
    ordering = ['-id']
    min_price=0
    max_price=0
    queryset = Products.objects.all()
    slug_field = 'slug'
    # paginate_by = 2
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginate_by = self.paginate_by
        categories = Categories.objects.all()
        brands = Brands.objects.all()
        variations = VariationProducts.objects.order_by('price')
        min_price_variation = variations.first()
        max_price_variation = variations.last()
        # min_attribute_value = Attributs.objects.filter(variation__id=7).aggregate(Min('name'))['name__min']
        # max_attribute_value = Attributs.objects.filter(variation__id=7).aggregate(Max('name'))['name__max']
        # min_charging = Attributs.objects.filter(variation__id=6).aggregate(Min('name'))['name__min']
        # max_charging= Attributs.objects.filter(variation__id=6).aggregate(Max('name'))['name__max']
        
        variations = Variations.objects.all()
        
        

        # for variation in variations:
        #     if variation.status == 2:
        #         attrs = Attributs.objects.filter(variation=variation)
        #         min_attr_for_attrs = attrs.aggregate(Min('name'))['name__min']
        #         max_attr_for_attrs = attrs.aggregate(Max('name'))['name__max']
        #         context['min_attr_for_var_{}'.format(variation.id)] = min_attr_for_attrs
        #         print('min_attr_for_var_{}'.format(variation.id))
        #         context['max_attr_for_var_{}'.format(variation.id)] = max_attr_for_attrs
        context['selected_slider_value'] = self.request.GET.get('slider_value')
        context['variations'] = variations
        context['categories'] = categories
        context['brands'] = brands
        context['paginate_by'] = paginate_by
        context['categories'] = categories
        context['min_price_variation'] = min_price_variation.price
        context['max_price_variation'] = max_price_variation.price
        # context['weightmin'] = float(min_attribute_value)
        # context['weightmax'] = (max_attribute_value)
        # context['min_charging'] = (min_charging)
        # context['max_charging'] = (max_charging)
        context['page'] = self.get_queryset()
        return context
    
    def get(self, request, *args, **kwargs):
        self.min_price = request.session.get('min_price', 0)
        self.max_price = request.session.get('max_price', 0)
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('min_price') is not None and request.POST.get('max_price') is not None:
            self.min_price = float(request.POST.get('min_price'))
            self.max_price = float(request.POST.get('max_price'))
            #сохранение знаечений в сессии
            request.session['min_price'] = self.min_price
            request.session['max_price'] = self.max_price

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        selected_brands = self.request.GET.getlist('brand')
        selected_variaty_types = []
        min_price = self.request.session.get('min_price')
        max_price = self.request.session.get('max_price')
        # for variete_obj in Attributs.objects.all():
        #     # Филтрация для вариаций с выбором
        #     if variete_obj.variation.status == 1:
        #         variaty_type = self.request.GET.getlist('variation_attr_{}'.format(variete_obj.id))
        #     selected_variaty_types.extend(variaty_type)
        # if selected_variaty_types:
        #     queryset = queryset.filter(variationproduct__attributs__id__in = selected_variaty_types)

        for variate in Variations.objects.filter(status = 2):
            #фильтрация для  вариациий с цифрами
            variaty_values =  self.request.GET.getlist('{}'.format(variate.id)) 
            if  variaty_values != ['',''] and variaty_values != []:
                queryset = queryset.filter(variationproduct__attributs__variation__id=variate.id, variationproduct__attributs__name__gte=float(variaty_values[0]), variationproduct__attributs__name__lte=float(variaty_values[1]))
        
        for variate in Variations.objects.filter(status = 1):
            variaty_type = self.request.GET.getlist('variation_attr_{}'.format(variate.id))
            selected_variaty_types = ''.join(variaty_type).split()
            if selected_variaty_types:
                queryset = queryset.filter(variationproduct__attributs__id = selected_variaty_types[0])

        if selected_brands:
            queryset = queryset.filter(brand__in=selected_brands)

        if min_price and max_price:
            if int(min_price) != 0 or int(max_price) != 0:
                queryset = queryset.filter(variationproduct__price__gte=self.min_price, variationproduct__price__lte=self.max_price+1)

        # print("selected_variaty   ",selected_variaty_types)
        # weightfrom = self.request.GET.get('7from')
        # weightto = self.request.GET.get('7to')
        # chargefrom = self.request.GET.get('6from')
        # chargeto = self.request.GET.get('6to')
        # speedsfrom = self.request.GET.get('5from')
        # speedsto = self.request.GET.get('5to')
        # voltagefrom = self.request.GET.get('3from')
        # voltageto = self.request.GET.get('3to')
        # selected_materials = self.request.GET.getlist('2selected-attr-id-of-variation')
        # selected_engine =  self.request.GET.getlist('1selected-attr-id-of-variation')
        # selected_battery =  self.request.GET.getlist('4selected-attr-id-of-variation')


        # print(selected_brands)
        # print(min_price, max_price)
        # print("сообщение из shop")
        # print("BEC : " , weightfrom, weightto)
        # print(selected_materials)
        # # if selected_brands:



        #     if int(min_price) != 0 or int(self.max_price) != 0:
        #         queryset = queryset.filter(brand__in=selected_brands, variationproduct__price__gte=self.min_price, variationproduct__price__lte=self.max_price+1)
        #         print(f"Теги выбраны. Цена выбрана  min_price: {int(self.min_price)}, max_price: {int(self.max_price)}")  # Вывод значений
        #     else:
        #         queryset = queryset.filter( Q(brand__in=selected_brands))
        #         print(f"Теги выбраны. Цена не выбрана  min_price: {int(self.min_price)}, max_price: {int(self.max_price)}")  # Вывод значений
        # else:
        #     if int(min_price) != 0 or int(self.max_price) != 0:
        #         queryset = queryset.filter(variationproduct__price__gte=self.min_price, variationproduct__price__lte=self.max_price+1)
        #         print(f"Теги не выбраны цена выбрана  min_price: {int(self.min_price)}, max_price: {int(self.max_price)}")  # Вывод значений
        #     else:
        #         pass






        # brand_filter = Q()
        # if selected_brands:
        #     brand_filter = Q(brand__in=selected_brands)

        # price_filter = Q()
        # if min_price and max_price:
        #     if int(min_price) != 0 or int(max_price) != 0:
        #         price_filter = Q(variationproduct__price__gte=min_price, variationproduct__price__lte=max_price + 1)

        # weight_filter = Q()
        # if weightfrom and weightto:
        #     weight_filter = Q(variationproduct__attributs__variation__id=7, variationproduct__attributs__name__gte=weightfrom, variationproduct__attributs__name__lte=weightto)

        # chagretime_filter = Q()
        # if  chargeto and chargefrom:
        #     chagretime_filter = Q(variationproduct__attributs__variation__id=6, variationproduct__attributs__name__gte=chargefrom, variationproduct__attributs__name__lte=chargeto)

        # speeds_filter = Q()
        # if  speedsto and speedsfrom:
        #     speeds_filter = Q(variationproduct__attributs__variation__id=5, variationproduct__attributs__name__gte=speedsfrom, variationproduct__attributs__name__lte=speedsto)
        
        # voltage_filter = Q()
        # if  voltageto and voltagefrom:
        #     voltage_filter = Q(variationproduct__attributs__variation__id=3, variationproduct__attributs__name__gte=voltagefrom, variationproduct__attributs__name__lte=voltageto)

        # material_filter = Q()
        # if selected_materials:
        #     for item in selected_materials:
        #         material_filter |= Q(variationproduct__attributs__id=int(item))
        # print(queryset.filter(material_filter))

        # engine_filter = Q()
        # if selected_materials:
        #     engine_filter = Q(variationproduct__attributs__id__in=selected_engine)

        # # Применяем фильтры к запросу
        # queryset = queryset.filter(brand_filter & price_filter & weight_filter & chagretime_filter & speeds_filter & voltage_filter & material_filter & engine_filter)





        # query_filter = Q()

        # # Фильтр по бренду
        # if selected_brands:
        #     query_filter &= Q(brand__in=selected_brands)

        # # Фильтр по цене
        # if min_price and max_price:
        #    if int(min_price) != 0 or int(max_price) != 0:
        #     query_filter = Q(variationproduct__price__gte=min_price, variationproduct__price__lte=max_price + 1)

        # # Фильтр по весу
        # if weightfrom and weightto:
        #     query_filter &= Q(variationproduct__attributs__variation__id=7, variationproduct__attributs__name__gte=int(weightfrom), variationproduct__attributs__name__lte=int(weightto))

        # # Фильтр по времени зарядки
        # if chargefrom and chargeto:
        #     query_filter &= Q(variationproduct__attributs__variation__id=6, variationproduct__attributs__name__gte=chargefrom, variationproduct__attributs__name__lte=chargeto)

        # # Фильтр по скорости
        # if speedsfrom and speedsto:
        #     query_filter &= Q(variationproduct__attributs__variation__id=5, variationproduct__attributs__name__gte=speedsfrom, variationproduct__attributs__name__lte=speedsto)

        # # Фильтр по напряжению
        # if voltagefrom and voltageto:
        #     query_filter &= Q(variationproduct__attributs__variation__id=3, variationproduct__attributs__name__gte=voltagefrom, variationproduct__attributs__name__lte=voltageto)

        # # Фильтр по материалу
        # if selected_materials:
        #     query_filter &= Q(variationproduct__attributs__id__in=selected_materials)

        # # Фильтр по двигателю
        # if selected_engine:
        #     query_filter &= Q(variationproduct__attributs__id__in=selected_engine)
        # print(query_filter, Products.objects.filter(query_filter))
        # # Применяем фильтр к queryset
        # queryset = queryset.filter(query_filter)
        
        # paginator = Paginator(queryset, self.paginate_by)
        # page_number = self.request.GET.get('page')
        # page = paginator.get_page(int(page_number))
        # print(paginator.get_page(2).object_list, page_number)

        self.request.session['min_price'] = 0
        self.request.session['max_price'] = 0
        return queryset
    
    # def get(self, request, *args, **kwargs):
    #     self.min_price = request.session.get('min_price', 0)
    #     self.max_price = request.session.get('max_price', 0)
    #     return super().get(request, *args, **kwargs)
    
    # def post(self, request, *args, **kwargs):
    #     if request.POST.get('min_price') is not None and request.POST.get('max_price') is not None:
    #         self.min_price = float(request.POST.get('min_price'))
    #         self.max_price = float(request.POST.get('max_price'))
    #         #сохранение знаечений в сессии
    #         request.session['min_price'] = self.min_price
    #         request.session['max_price'] = self.max_price

        # data = {
        #     'success': True,
        #     'количество подходящих продуктов': Products.objects.filter(variationproduct__price__gte=int(float(self.min_price)), variationproduct__price__lte=int(float(self.max_price))).count(),
        #     'min' : self.min_price,
        #     'max' : self.max_price
        # }
        # return JsonResponse(data)
    
    # def get_queryset(self):
    #     queryset = Products.objects.all()
    #     cat_id = self.request.GET.get('cat_id')  # Получаем значение id тега из GET-параметра
    #     if cat_id:
    #         cate = get_object_or_404(Categories, id=cat_id)  # Получаем объект тега по его id
    #         queryset = queryset.filter(category=cate).distinct() # Фильтруем продукты по выбранному тегу
    #     selected_brands = self.request.GET.getlist('brand')
    #     if self.request.build_absolute_uri() == 'http://127.0.0.1:8000/shop/':
    #         pass
    #     else:
    #         try:
    #             id = int(self.request.build_absolute_uri().split("id=")[-1].strip())
    #             queryset = queryset.filter(category__id=id).distinct()
    #             self.request.session['id'] = id
    #         except:
    #             try:
    #                 id = self.request.session.get('id')
    #                 queryset = queryset.filter(category__id=id).distinct()
    #             except:
    #                 pass

    #     if selected_brands != []:
    #         if int(self.min_price) != 123 or int(self.max_price) != 1230:
    #             queryset = queryset.filter( (Q(brand__in=selected_brands) | Q(variationproduct__price__gte=self.min_price, variationproduct__price__lte=self.max_price+1)))
    #             print(f"ИСКЛЮЧЕИЕ НЕ СРАБОТАЛО  min_price: {int(self.min_price)}, max_price: {int(self.max_price)}")  # Вывод значений
    #         else:
    #             queryset = queryset.filter( Q(brand__in=selected_brands))
    #             print(f"ИСКЛЮЧЕИЕ СРАБОТАЛО     min_price: {int(self.min_price)}, max_price: {int(self.max_price)}") 

    #     return queryset



def get_price_variations(request):
    min_price_variation = VariationProducts.objects.order_by('price').first()
    max_price_variation = VariationProducts.objects.order_by('-price').first()
    
    data = {
        'min_price': min_price_variation.price,
        'max_price': max_price_variation.price,
    }
    
    return JsonResponse(data)


class ProductSearch(ListView):
    model = Products
    template_name = 'shops/searchshop.html'
    context_object_name = 'products'

    

# class ShopFilter(ProductShop):
#     def get(self, request, *args, **kwargs):
#         self.min_price = request.session.get('min_price', 0)
#         self.max_price = request.session.get('max_price', 0)
#         return super().get(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         if request.POST.get('min_price') is not None and request.POST.get('max_price') is not None:
#             self.min_price = float(request.POST.get('min_price'))
#             self.max_price = float(request.POST.get('max_price'))
#             #сохранение знаечений в сессии
#             request.session['min_price'] = self.min_price
#             request.session['max_price'] = self.max_price

#         data = {
#             'success': True,
#             'количество подходящих продуктов': Products.objects.filter(variationproduct__price__gte=int(float(self.min_price)), variationproduct__price__lte=int(float(self.max_price))).count(),
#             'min' : self.min_price,
#             'max' : self.max_price
#         }
#         return JsonResponse(data)

#     def get_queryset(self):
#         queryset = self.filtered_queryset
#         # selected_categories = self.request.GET.getlist('category')
#         selected_brands = self.request.GET.getlist('brand')
#         # slug = self.request.session.get('cat_slug')
#         # print("sdasd " + self.request.build_absolute_uri())
#         # print(slug)
#         # queryset = queryset.filter(brand__in=selected_brands, category__slug=slug)
#         print(queryset)
#         if int(self.min_price) != 123 or int(self.max_price) != 1230:
#             queryset = queryset.filter( (Q(brand__in=selected_brands) | Q(variationproduct__price__gte=self.min_price, variationproduct__price__lte=self.max_price+1)))
#             print(f"ИСКЛЮЧЕИЕ НЕ СРАБОТАЛО  min_price: {int(self.min_price)}, max_price: {int(self.max_price)}")  # Вывод значений
#         else:
#             queryset = queryset.filter( Q(brand__in=selected_brands))
#             print(f"ИСКЛЮЧЕИЕ СРАБОТАЛО     min_price: {int(self.min_price)}, max_price: {int(self.max_price)}") 
#         # paginator = Paginator(queryset, self.paginate_by)
#         # page_number = self.request.GET.get('page')
#         # page = paginator.get_page(page_number)
#         return queryset
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         paginate_by = self.paginate_by
#         categories = Categories.objects.all()
#         brands = Brands.objects.all()
#         variations = VariationProducts.objects.order_by('price')
#         min_price_variation = variations.first()
#         max_price_variation = variations.last()
#         context['brands'] = brands
#         context['paginate_by'] = paginate_by
#         context['categories'] = categories
#         context['min_price_variation'] = min_price_variation.price,
#         context['max_price_variation'] = max_price_variation.price,
#         return context



class CategoriesShops(ListView):
    model = Products
    template_name = 'shops/shop.html'
    context_object_name = 'products'
    slug_field = 'slug'
    ordering = ['-id']
    # paginate_by = 2
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginate_by = self.paginate_by
        categories = Categories.objects.all()
        brands = Brands.objects.all()
        variations = VariationProducts.objects.order_by('price')
        min_price_variation = variations.first()
        max_price_variation = variations.last()
        context['brands'] = brands
        context['paginate_by'] = paginate_by
        context['categories'] = categories
        context['min_price_variation'] = min_price_variation.price,
        context['max_price_variation'] = max_price_variation.price,
        return context
    def get(self, request, *args, **kwargs):
        self.min_price = request.session.get('min_price', 0)
        self.max_price = request.session.get('max_price', 0)
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('min_price') is not None and request.POST.get('max_price') is not None:
            self.min_price = float(request.POST.get('min_price'))
            self.max_price = float(request.POST.get('max_price'))
            #сохранение знаечений в сессии
            request.session['min_price'] = self.min_price
            request.session['max_price'] = self.max_price

        data = {
            'success': True,
            'количество подходящих продуктов': Products.objects.filter(variationproduct__price__gte=int(float(self.min_price)), variationproduct__price__lte=int(float(self.max_price))).count(),
            'min' : self.min_price,
            'max' : self.max_price
        }
        return JsonResponse(data)
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        slug = self.kwargs.get('slug')
        print("ГЛАВНЫЙ СЛАГ " + slug)
        self.request.session['cat_slug'] = slug
        queryset = Products.objects.filter(category__slug=slug)
        selected_brands = self.request.GET.getlist('brand')
        min_price = self.request.session.get('min_price')
        max_price = self.request.session.get('max_price')
        print(selected_brands)
        print(min_price, max_price)
        print('сообщение из filter')
        if selected_brands:
            if int(min_price) != 0 or int(self.max_price) != 0:
                queryset = queryset.filter(brand__in=selected_brands, variationproduct__price__gte=self.min_price, variationproduct__price__lte=self.max_price+1)
                print(f"Теги выбраны. Цена выбрана  min_price: {int(self.min_price)}, max_price: {int(self.max_price)}")  # Вывод значений
            else:
                queryset = queryset.filter( Q(brand__in=selected_brands))
                print(f"Теги выбраны. Цена не выбрана  min_price: {int(self.min_price)}, max_price: {int(self.max_price)}")  # Вывод значений
        else:
            if int(min_price) != 0 or int(self.max_price) != 0:
                queryset = queryset.filter(variationproduct__price__gte=self.min_price, variationproduct__price__lte=self.max_price+1)
                print(f"Теги не выбраны цена выбрана  min_price: {int(self.min_price)}, max_price: {int(self.max_price)}")  # Вывод значений
            else:
                pass
        
        self.request.session['min_price'] = 0
        self.request.session['max_price'] = 0
        return queryset
        
        # if int(self.min_price) != 123 or int(self.max_price) != 1230:
        #     queryset = queryset.filter( (Q(brand__in=selected_brands) | Q(variationproduct__price__gte=self.min_price, variationproduct__price__lte=self.max_price+1)))
        #     print(f"ИСКЛЮЧЕИЕ НЕ СРАБОТАЛО  min_price: {int(self.min_price)}, max_price: {int(self.max_price)}")  # Вывод значений
        # else:
        #     queryset = queryset.filter( Q(brand__in=selected_brands))
        #     print(f"ИСКЛЮЧЕИЕ СРАБОТАЛО     min_price: {int(self.min_price)}, max_price: {int(self.max_price)}") 
        # paginator = Paginator(queryset, self.paginate_by)
        # page_number = self.request.GET.get('page')
        # page = paginator.get_page(page_number)
        return queryset


class AddToCartView(View):
    def get(self, request, *args, **kwargs):
        product_slug = kwargs.get('slug')
        cart = Carts.objects.get_or_create(owner = request.user, in_order=False)
        print(cart)
        product =  Products.objects.get(slug = product_slug)
        recalc_cart(cart[0])
        cart[0].save()
        cart_product, created = CartProduct.objects.get_or_create(user=request.user, card=cart[0], product=product)
        
        print(created)
        if created==False:
            
            cart_product.qty += 1
            cart_product.save()
        else:
            cart[0].save()
            cart[0].products.add(cart_product)
            cart[0].save()
            recalc_cart(cart[0])
            cart[0].save()
        return HttpResponseRedirect('/cart/')

class CartView(View):

    def get(self, request, *args, **kwargs):
        cart = Carts.objects.get_or_create(owner = request.user, in_order = False)
        context ={
            'cart':cart[0],
            
        }
        return render(request, 'shops/cart.html', context)
    
class ChangeQTY(View):
    def post(self, request, *args, **kwargs):
        print(request.POST)
        product_slug = kwargs.get('slug')
        product =  Products.objects.get(slug = product_slug)
        cart = Carts.objects.get_or_create(owner = request.user, in_order=False)
        cart_product = CartProduct.objects.get(user=request.user, card=cart[0], product=product)
        qty = int(request.POST.get('qty'))
        print(qty)
        cart_product.qty = qty
        cart_product.save()
        recalc_cart(cart[0])
        # cart[0].save()
        return HttpResponseRedirect('/cart/')

class DeleteProductFromCart(View):
    def post(self, request, *args, **kwargs):
        print(request.POST)
        product_slug = kwargs.get('slug')
        product =  Products.objects.get(slug = product_slug)
        cart = Carts.objects.get_or_create(owner = request.user, in_order=False)
        cart_product = CartProduct.objects.get(user=request.user, card=cart[0], product=product)
        cart_product.delete()
        recalc_cart(cart[0])
        # cart[0].save()
        return HttpResponseRedirect('/cart/')
    
class CheckoutView(View):

    def get(self, request, *args, **kwargs):
        cart = Carts.objects.get(owner = request.user, in_order=False)
        form = OrderForm(request.POST or None)
        default_address = Adress.objects.get(default=True)
        context ={
            'cart':cart,
            'form':form,
            'address':default_address,
        }
        return render(request, 'shops/checkout.html', context)
    
class MakeOrderView(View):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.user = request.user
            # new_order.first_name = form.cleaned_data['first_name']
            # new_order.last_name = form.cleaned_data['last_name']
            # new_order.company_name = form.cleaned_data['company_name']
            # new_order.country = form.cleaned_data['country']
            # new_order.city = form.cleaned_data['city']
            # new_order.street = form.cleaned_data['street']
            # new_order.postcode = form.cleaned_data['postcode']
            # new_order.appartament = form.cleaned_data['appartament']
            # new_order.email = form.cleaned_data['email']
            # new_order.phone = form.cleaned_data['phone']
            # new_order.notes = form.cleaned_data['notes']
            cart = Carts.objects.get(owner = request.user, in_order=False)
            new_order.address = Adress.objects.get(default=True)
            new_order.order_sum = int(cart.final_price)
            new_order.cart = cart
            new_order.save()
            cart.in_order = True
            cart.save()
            new_order.save()
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/checkout/')

class WishListView(ListView):
    # model = WishList
    # context_object_name = 'wishlist'
    # template_name = 'shops/wishlist.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        
    #     context['products'] = WishList.objects.get(user=self.request.user).product

    #     return context
    def get(self, request, *args, **kwargs):
        context ={
            'wishlist' : WishList.objects.get_or_create(user = self.request.user)[0],
            'products' : WishList.objects.get_or_create(user=self.request.user)[0].product.all(),
        }

        return render(request, 'shops/wishlist.html', context)


class AddToWishList(View):
    def get(self, request, *args, **kwargs):
        product_slug = kwargs.get('slug')
        wishlist = WishList.objects.get_or_create(user = request.user)
        product =  Products.objects.get(slug = product_slug)
        product_in_wishlist = WishList.objects.filter(user=request.user, product__slug=product_slug)
        print(product_in_wishlist)
        if not product_in_wishlist:
            wishlist[0].product.add(product)
            wishlist[0].save()

        return HttpResponseRedirect('/product/' + product_slug)
    
class RemoveFromWishList(View):
    def get(self, request, *args, **kwargs):
        product_slug = kwargs.get('slug')
        wishlist = WishList.objects.get_or_create(user = request.user)
        product =  Products.objects.get(slug = product_slug)
        product_in_wishlist = WishList.objects.filter(user=request.user, product__slug=product_slug)
        if product_in_wishlist:
            wishlist[0].product.remove(product)
            wishlist[0].save()

        return HttpResponseRedirect('/wishlist/')
    
class SearchView(TemplateView):
    template_name = 'search.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ProductSearchForm(self.request.GET)
        selected_category = self.request.GET.get('category')
        if form.is_valid():
            search_description = form.cleaned_data.get('search_description')
            if selected_category != "None" and selected_category != None:
                product = Products.objects.filter(description__icontains = search_description, category = Categories.objects.get(id = selected_category))
                print('запрос 2')
            else:
                print('запрос 1')
                product = Products.objects.filter(description__icontains = search_description)
        else:
            product = Products.objects.all()
        context['products'] = product
        context['form'] = form 
              
        return context