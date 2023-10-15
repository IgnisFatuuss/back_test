from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Adress


@receiver(post_save, sender = Adress)
def update_address(sender, instance, created, **kwargs):
    if instance.default is True:
        Adress.objects.filter(user=instance.user, default=True).exclude(pk=instance.pk).update(default=False)