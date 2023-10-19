from django import template
from Profile.models import Profile,Adress

register = template.Library()

@register.simple_tag(takes_context=True)
def addresstag(context):
    request = context['request']
    try:
        return Adress.objects.get(user = request.user, default = True)
    except Adress.DoesNotExist:
        return None

@register.simple_tag(takes_context=True)
def profiletag(context):
    request = context['request']
    try:
        return Profile.objects.get(user = request.user)
    except Profile.DoesNotExist:
        return None