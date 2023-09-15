from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget 
from django import forms
from nested_admin import NestedTabularInline



class VariationsInline(NestedTabularInline):
    model = Variations
    extra = 3

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

class GallereisInline(NestedTabularInline):
    model = Gallereis
    extra = 1


class ProductsAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание',widget=CKEditorUploadingWidget())
    class Meta:
        model = Products
        fields = '__all__'

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    form = ProductsAdminForm
    inlines = [VariationsInline, FaqsInline, ReviewsInline, EmotionsInline]

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

@admin.register(Variations)
class VariationsAdmin(admin.ModelAdmin):
    inlines = [AttributsInline, GallereisInline]


admin.site.register(Orders)
admin.site.register(Cards)
admin.site.register(Faqs)
admin.site.register(Reviews)
admin.site.register(Emotions)


