from django import template
from shops.models import *

register = template.Library()

@register.simple_tag(takes_context=True)
def wishtag(context):
    request = context['request']
    try:
        return WishList.objects.get_or_create(user = request.user)[0]
    except:
        return None
