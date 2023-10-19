from django import template
from shops.models import *

register = template.Library()

@register.simple_tag(takes_context=True)
def carttag(context):
    request = context['request']
    try:
        return Carts.objects.get_or_create(owner = request.user, in_order = False)[0]
    except:
        return None
