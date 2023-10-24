from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget 
from django import forms
from nested_admin import NestedTabularInline, NestedModelAdmin
from modeltranslation.admin import TranslationAdmin


class GallereisInline(NestedTabularInline):
    model = Gallereis
    extra = 1

class VariationsProductInline(NestedTabularInline):
    model = VariationProducts
    inlines = [GallereisInline]
    extra = 1

class AttributsInline(admin.TabularInline):
    model = Attributs
    extra = 1

class FaqsInline(NestedTabularInline):
    model = Faqs
    extra = 1

class ReviewsInline(NestedTabularInline):
    model = Reviews
    extra = 1
    
class EmotionsInline(NestedTabularInline):
    model = Emotions
    extra = 1


class ProductsAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label='Описание',widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label='Описание',widget=CKEditorUploadingWidget())
    class Meta:
        model = Products
        fields = '__all__'

class StoresAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание',widget=CKEditorUploadingWidget())
    class Meta:
        model = Stores
        fields = '__all__'

@admin.register(Products)
class ProductsAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('name',),}
    form = ProductsAdminForm
    inlines = [VariationsProductInline, FaqsInline, ReviewsInline, EmotionsInline]

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    list_display = ['name', 'id']

@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

@admin.register(Variations)
class VariationsAdmin(admin.ModelAdmin):
    inlines = [AttributsInline,]

@admin.register(Stores)
class StoresAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    form = StoresAdminForm

# @admin.register(VariationProducts)
# class VariationProductAdmin(admin.ModelAdmin):
#     inlines = [GallereisInline,]
admin.site.register(Carts)
admin.site.register(CartProduct)
admin.site.register(Orders)
admin.site.register(WishList)
admin.site.register(Faqs)
admin.site.register(Reviews)
admin.site.register(Emotions)
admin.site.register(SliderProduct)
admin.site.register(Banners)
# admin.site.register(Gallereis)


