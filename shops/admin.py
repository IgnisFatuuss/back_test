from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget 
from django import forms

# Register your models here.

class ProductsAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание',widget=CKEditorUploadingWidget())
    class Meta:
        model = Products
        fields = '__all__'


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    form = ProductsAdminForm

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

admin.site.register(Variations)
admin.site.register(Attributs)
admin.site.register(Orders)
admin.site.register(Cards)
admin.site.register(Faqs)
admin.site.register(Reviews)
admin.site.register(Emotions)
admin.site.register(Gallereis)


