from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Products)
class ProductsTranslationOptions(TranslationOptions):
    fields = ('name', 'description', )

@register(Categories)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Tags)
class TagsTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Brands)
class BrandsTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Variations)
class VariationsTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Attributs)
class AttributsTranslationOptions(TranslationOptions):
    fields = ('name', )