from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from faicon.fields import FAIconField

class GeneralSettings(models.Model):
    logo = models.ImageField("Логотип", blank=True, null=True)
    favicon = models.ImageField("Фавикон", blank=True, null=True)
    name = models.CharField("Название", max_length=500, blank=True, null=True)
    content = models.TextField("Контент", max_length=500, blank=True, null=True)
    pn_pt = models.CharField("ПН-ПТ", max_length=500, blank=True, null=True)
    sb = models.CharField("СБ", max_length=500, blank=True, null=True)
    vs = models.CharField("ВС", max_length=500, blank=True, null=True)
    def __str__(self):
        return "Общая настройка"

    class Meta:
        verbose_name = 'Общая настройка'
        verbose_name_plural = 'Общие настройки'
class Phones(models.Model):
    phone = models.CharField(blank=True, verbose_name='Телефон', max_length=150)
    generalsettings = models.ForeignKey(GeneralSettings, verbose_name='Настройки', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

class Contacts(models.Model):
    address = models.CharField(max_length=100, blank=True, verbose_name='Адресс')
    city = models.CharField(max_length=100, blank=True, verbose_name='Город')
    zip_code = models.CharField(max_length=100, blank=True, verbose_name='Почтовый индекс')
    general_settings = models.ForeignKey(GeneralSettings, verbose_name='Настройки', on_delete=models.SET_NULL, null=True, blank=True)
    region = models.ForeignKey('Regions', verbose_name='Настройки', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

class Social(models.Model):
    link = models.SlugField("Ссылка", max_length=500, null=True)
    icon = FAIconField()
    general_settings = models.ForeignKey(GeneralSettings, verbose_name='Настройки', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

class Pages(models.Model):
    data = models.DateTimeField(auto_now=True)
    name = models.CharField("Название", max_length=500, null=True)
    content = models.TextField("Контент", max_length=500, null=True)
    title = models.CharField("Заголовок", max_length=500, null=True)
    description = models.TextField("Описание", max_length=500, null=True)
    slug = models.SlugField("Ссылка", max_length=160, unique=True)
    header = models.BooleanField("Шапка", default=False)
    footer = models.BooleanField("Подвал", default=False)

    def get_absolute_url(self):
        return reverse('pages', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

class Rubric(models.Model):
    image = models.ImageField("Изображение", upload_to="categories/images/")
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Родитель')
    name = models.CharField("Название", max_length=500, null=True)
    content = models.TextField("Контент", max_length=500, null=True)
    title = models.CharField("Заголовок", max_length=500, null=True)
    description = models.TextField("Описание", max_length=500, null=True)
    slug = models.SlugField("Ссылка", max_length=160, unique=True)

    def get_absolute_url(self):
        return reverse('categories', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Blogs(models.Model):
    data = models.DateTimeField(auto_now=True)
    name = models.CharField("Название", max_length=500, null=True)
    content = models.TextField("Контент", max_length=500, null=True)
    title = models.CharField("Заголовок", max_length=500, null=True)
    description = models.TextField("Описание", max_length=500, null=True)
    slug = models.SlugField("Ссылка", max_length=160, unique=True)
    rubric = models.ForeignKey('Rubric', verbose_name="Категория", on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField('Tags', verbose_name='Метки', blank=True)

    def get_absolute_url(self):
        return reverse('blogs', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Commentaries(models.Model):
    data = models.DateTimeField(auto_now=True)
    content = models.TextField("Контент", max_length=500, null=True)
    blogs = models.ForeignKey(Blogs, verbose_name="Категория", on_delete=models.SET_NULL, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='channel')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class Faq(models.Model):
    data = models.DateTimeField(auto_now=True)
    question = models.CharField("Вопрос", max_length=500, null=True)
    answer = models.TextField("Ответ", max_length=500, null=True)
    slug = models.SlugField("Ссылка", max_length=160, unique=True)

    def get_absolute_url(self):
        return reverse('faqs', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Часто задаваемый вопрос'
        verbose_name_plural = 'Часто задаваемые вопросы'

class Tags(models.Model):
    image = models.ImageField("Изображение", upload_to="tags/images/")
    name = models.CharField("Название", max_length=500, null=True)
    content = models.TextField("Контент", max_length=500, null=True)
    slug = models.SlugField("Ссылка", max_length=160, unique=True)

    def get_absolute_url(self):
        return reverse('blogs', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'

class Regions(models.Model):
    image = models.ImageField("Изображение", upload_to="regions/images/")
    name = models.CharField("Название", max_length=500, null=True)
    slug = models.SlugField("Ссылка", max_length=160, unique=True)

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

class Helps(models.Model):
    data = models.DateTimeField(auto_now=True)
    name = models.CharField("Название", max_length=500, null=True)
    content = models.TextField("Контент", max_length=500, null=True)
    title = models.CharField("Заголовок", max_length=500, null=True)
    description = models.TextField("Описание", max_length=500, null=True)
    slug = models.SlugField("Ссылка", max_length=160, unique=True)

    def get_absolute_url(self):
        return reverse('pages', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководство'


