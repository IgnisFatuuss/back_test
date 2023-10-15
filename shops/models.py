from django.db import models
from django.contrib.auth.models import User
from Profile.models import Adress
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя')
    article = models.CharField( max_length=250, verbose_name='Артикль')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')
    description = models.TextField(verbose_name='Описание')
    available = models.BooleanField(default=True, verbose_name='Доступность')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField( auto_now_add=True, verbose_name='Обновлено')
    category = models.ManyToManyField('categories', verbose_name='Категория', related_name='categories')
    tag = models.ManyToManyField('tags', verbose_name='Тэг', related_name='tags')
    brand = models.ForeignKey('brands', on_delete=models.PROTECT, verbose_name='Брэнд', null=True)

    def __str__(self):
        return self.name

     
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class Categories(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')
    img = models.ImageField(upload_to='shops/categories/', verbose_name='Изображение')
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
    logo = models.ImageField(upload_to='shops/brands/', verbose_name='Логотип')

    class Meta:
        verbose_name = 'Брэнд'
        verbose_name_plural = 'Брэнды'
    
    def __str__(self):
        return self.name

class VariationProducts(models.Model):
    product = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name='Товар', related_name='variationproduct')
    price = models.PositiveIntegerField(verbose_name='Цена')
    attributs = models.ManyToManyField('Attributs', verbose_name='Аттрибуты')

    class Meta:
        verbose_name = 'Вариация продуктов'
        verbose_name_plural = 'Вариации продуктов'

class Variations(models.Model):
    STATUS = [(1, 'Выбор'), (2, 'Цифры')]
    status = models.PositiveIntegerField(default=1, choices=STATUS, blank=True, null=True, verbose_name='Статус')
    name = models.CharField(max_length=255, verbose_name='Имя')
    participate = models.BooleanField(verbose_name='Участвовать в варицациях',blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вариация'
        verbose_name_plural = 'Вариации'

class Attributs(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    variation = models.ForeignKey(Variations, on_delete=models.PROTECT, verbose_name='Вариации', related_name='attributs')
    
    def __str__(self):

        return str(self.variation) + " : " +str(self.name)
    
    class Meta:
        verbose_name = 'Атрибут'
        verbose_name_plural = 'Атрибуты'


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    STATUS = [(1, 'Не оплачено'), (2, 'Оплачено'),]
    status = models.PositiveIntegerField(default=1, choices=STATUS, blank=True, null=True, verbose_name='Статус')
    # first_name = models.CharField(max_length=255, verbose_name='Имя')
    # last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    # company_name = models.CharField(max_length=255, blank=True, verbose_name='Имя компании')
    # countries = [(1, 'Russia'), (2, 'USA'),]
    # country = models.PositiveIntegerField(choices=countries, verbose_name='Страна')
    # city = models.CharField(max_length=255, verbose_name='Город')
    # street = models.CharField(max_length=255, verbose_name='Улица')
    # postcode = models.CharField(max_length=255, verbose_name='Почтовый код')
    # appartament = models.CharField(max_length=255, blank=True, verbose_name='Апартаменты')
    # email = models.CharField(max_length=255, verbose_name='email')
    # phone = models.CharField(max_length=255, verbose_name='Телефон')
    address = models.ForeignKey(Adress, on_delete=models.CASCADE, verbose_name='Адрес', default=False, related_name='address')
    order_sum = models.PositiveIntegerField(verbose_name='Общая сумма')
    date = models.DateField(auto_now=True, verbose_name='Дата')
    notes = models.CharField(max_length=255, blank=True, verbose_name='Примечания')
    cart = models.ForeignKey('Carts', on_delete=models.CASCADE, verbose_name='Корзина')

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
    answer = models.TextField(verbose_name='Ответ', blank=True)
    question = models.TextField(verbose_name='Вопрос')
    product = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name='Продукт', related_name='faqs')
    date = models.DateField(auto_now=True, verbose_name='Дата')
    
    class Meta:
        verbose_name = 'Часто задаваемые вопросы'
        verbose_name_plural = 'Часто задаваемые вопросы'

class Reviews(models.Model):
    product = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name='Продукт', related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    date = models.DateField(auto_now=True, verbose_name='Дата')
    text = models.TextField(verbose_name='Текст')
    review = models.PositiveIntegerField(verbose_name='Отзыв', validators=[
            MinValueValidator(1, message='Review must be at least 1'),
            MaxValueValidator(5, message='Review cannot be more than 5')
        ])

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
    image = models.ImageField(upload_to='shops/', verbose_name='Картинка')
    variations = models.ForeignKey(VariationProducts, on_delete=models.PROTECT, verbose_name='Вариация', related_name='gallereis')

    
    class Meta:
        verbose_name = 'Галлерея'
        verbose_name_plural = 'Галлереи'

class CartProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    card = models.ForeignKey('Carts', verbose_name='Kорзина', on_delete=models.CASCADE, related_name='related_products')
    product = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name='Продукт')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def save(self, *args, **kwargs):
        self.final_price = self.qty * VariationProducts.objects.get(product=self.product).price
        super().save(*args,**kwargs)

class Carts(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    products = models.ManyToManyField(CartProduct, blank=True, related_name='cart', verbose_name='Продукты')
    total_products = models.PositiveIntegerField(verbose_name='Количество продуктов',default=0)
    final_price = models.DecimalField(verbose_name='Цена', max_digits=9, decimal_places=2, default=0)
    in_order = models.BooleanField(default=False)
    for_anonymous = models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
    #     cart_data = self.products.aggregate(models.Sum('final_price'), models.Count('id'))
    #     if cart_data.get('final_price__sum'):
    #         self.final_price = cart_data['final_price__sum']
    #     else:
    #         self.final_price=0
    #     self.total_products = cart_data['id__count']
    #     super().save(*args,**kwargs)


    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    product = models.ManyToManyField(Products, blank=True, verbose_name='Продукт')


    class Meta:
        verbose_name = 'Список избранных товаров'
        verbose_name_plural = 'Список избранных товаров'