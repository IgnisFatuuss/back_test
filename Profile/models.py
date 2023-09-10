from django.db import models
from django.contrib.auth.models import User
from shops.models import Products
from django.urls import reverse

# Create your models here.


def get_user_dir(instance, filename) -> str:
    extension = filename.split(".")[-1]
    return f"users/user{instance.user.id}.{extension}"

class Profile(models.Model):
    """ Модель профиля пользователя """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to=get_user_dir, blank=True, verbose_name='Аватар', default='default/profile/profile-thumb.jpg')
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, verbose_name='Адресс')
    city = models.CharField(max_length=100, blank=True, verbose_name='Город')
    zip_code = models.CharField(max_length=100, blank=True, verbose_name='Почтовый индекс')
    phone = models.CharField(blank=True, verbose_name='Телефон', max_length=150)

    def str(self):
        return self.user.username

    def get_absolute_url(self):
        """ Абсолютный путь к объекту Profile """
        return reverse('user', kwargs={'pk': self.user.id})

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class Histories(models.Model):
    profile= models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name= 'Профиль')
    url = models.URLField(verbose_name='Ссылка')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Продукт')

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'
