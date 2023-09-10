from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя')
    article = models.CharField( max_length=250, verbose_name='Артикль')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')
    description = models.TextField(verbose_name='Описание')
    available = models.BooleanField(default=True, verbose_name='Доступность')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField( auto_now_add=True, verbose_name='Обновлено')
    category = models.ManyToManyField('categories', verbose_name='Категория')
    tag = models.ManyToManyField('tags', verbose_name='Тэг')
    brand = models.ForeignKey('brands', on_delete=models.PROTECT, verbose_name='Брэнд', null=True)

    def __str__(self):
        return self.name
     
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class Categories(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')
    img = models.ImageField(upload_to=None, verbose_name='Изображение')
    parent = models.ForeignKey('self', on_delete=models.PROTECT, related_name='child', verbose_name='Родитель', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
class Tags(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
    
    def __str__(self):
        return self.name

class Brands(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')
    logo = models.ImageField(upload_to=None, verbose_name='Логотип')

    class Meta:
        verbose_name = 'Брэнд'
        verbose_name_plural = 'Брэнды'
    
    def __str__(self):
        return self.name

class Variations(models.Model):
    products = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name='Продукт')
    STATUS = [(1, 'Выбор'), (2, 'Цифры')]
    status = models.PositiveIntegerField(default=1, choices=STATUS, blank=True, null=True, verbose_name='Статус')
    name = models.CharField(max_length=255, verbose_name='Имя')
    participate = models.BooleanField(verbose_name='Участвовать в варицациях',blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Вариация'
        verbose_name_plural = 'Вариации'

class Attributs(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    variation = models.ForeignKey(Variations, on_delete=models.PROTECT, verbose_name='Вариации')

    class Meta:
        verbose_name = 'Атрибут'
        verbose_name_plural = 'Атрибуты'


class Orders(models.Model):
    variation = models.ManyToManyField(Variations, verbose_name='Вариация')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    STATUS = [(1, 'Не оплачено'), (2, 'Оплачено')]
    status = models.PositiveIntegerField(default=1, choices=STATUS, blank=True, null=True, verbose_name='Статус')
    order_sum = models.PositiveIntegerField(verbose_name='Общая сумма')
    date = models.DateField(auto_now=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Cards(models.Model):
    variation = models.ManyToManyField(Variations, verbose_name='Вариации')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    order_sum = models.PositiveIntegerField(verbose_name='Общая сумма')   
    
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

class Faqs(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    answer = models.TextField(verbose_name='Ответ')
    question = models.TextField(verbose_name='Вопрос')
    product = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name='Продукт')
    date = models.DateField(auto_now=True, verbose_name='Дата')
    
    class Meta:
        verbose_name = 'Часто задаваемые вопросы'
        verbose_name_plural = 'Часто задаваемые вопросы'

class Reviews(models.Model):
    product = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name='Продукт')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    date = models.DateField(auto_now=True, verbose_name='Дата')
    text = models.TextField(verbose_name='Текст')
    review = models.PositiveIntegerField(verbose_name='Отзыв')

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'

class Emotions(models.Model):
    product = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name='Продукт')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    CHOICES = (('2', 'Дизлайк'),('1', 'Лайк'))
    rate = models.CharField(max_length=255, choices=CHOICES, verbose_name='Оценка')
    
    class Meta:
        verbose_name = 'Эмоция'
        verbose_name_plural = 'Эмоции'

class Gallereis(models.Model):
    image = models.ImageField(upload_to=None, verbose_name='Картинка')
    variations = models.ForeignKey(Variations, on_delete=models.PROTECT, verbose_name='Вариация')

    
    class Meta:
        verbose_name = 'Галлерея'
        verbose_name_plural = 'Галлереи'
