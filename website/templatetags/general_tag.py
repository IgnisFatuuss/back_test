from django import template
from website.models import *


register = template.Library()

@register.simple_tag()
def header_phone():
    try:
        return Phones.objects.get(id=1)
    except Phones.DoesNotExist:
        return None
    
@register.simple_tag()
def get_site_logo():
    return GeneralSettings.objects.first().logo.url

@register.simple_tag()
def get_site_name():
    return GeneralSettings.objects.first().name