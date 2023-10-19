from django import template
from website.models import Phones


register = template.Library()

@register.simple_tag()
def header_phone():
    try:
        return Phones.objects.get(id=1)
    except Phones.DoesNotExist:
        return None
    