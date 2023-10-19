from django import template
from shops.models import *
from shops.forms import ProductSearchForm

register = template.Library()

@register.inclusion_tag('searchform.html')
def productsearchform():
    form = ProductSearchForm
    return {'form' : form, 'categories' : Categories.objects.all(),}