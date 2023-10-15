from django.db import models
from django.contrib.auth.models import User
# from shops.models import Products
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
    # address = models.CharField(max_length=100, blank=True, verbose_name='Адрес')
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

class Adress(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    company_name = models.CharField(max_length=255, blank=True, verbose_name='Имя компании')
    countries = [(1, 'Russia'), (2, 'USA'),]
    country = models.PositiveIntegerField(choices=countries, verbose_name='Страна')
    city = models.CharField(max_length=255, verbose_name='Город')
    street = models.CharField(max_length=255, verbose_name='Улица')
    postcode = models.CharField(max_length=255, verbose_name='Почтовый код')
    appartament = models.CharField(max_length=255, blank=True, verbose_name='Апартаменты')
    email = models.CharField(max_length=255, verbose_name='email')
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    default = models.BooleanField(default=False, null=True, blank=False)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адресы'

class Histories(models.Model):
    profile= models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name= 'Профиль')
    url = models.URLField(verbose_name='Ссылка')

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'

# class User(AbstractUser):    
#     GENDER_CHOICE = [
#         (1, 'Мужской'),        (2, 'Женский'),
#     ]
#     TIME_ZONE = [        (1, '1'),
#         (2, '2'),        (3, '3'),
#     ]    
#     is_guest = models.BooleanField(default=False,verbose_name="Гость")
#     is_moderar = models.BooleanField(default=False,verbose_name="Админ")    
#     login_status = models.BooleanField(default=False,verbose_name="Статус")
#     blocked = models.BooleanField(default=False,verbose_name="Заблокирован")    
#     username = models.CharField(max_length=30, unique=True)
#     avatar = models.ImageField(upload_to=get_user_dir, blank=True, verbose_name='Аватар', default='default/profile/profile-thumb.jpg')    
#     birthday = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
#     age = models.IntegerField(verbose_name='Возвраст', blank=True, null=True)    
#     gender = models.PositiveSmallIntegerField('Пол', choices=GENDER_CHOICE,  blank=True, null=True)
#     time_zone = models.PositiveSmallIntegerField('Часовой пояс', choices=TIME_ZONE,  blank=True, null=True)    
#     sum_message = models.IntegerField("Сообщений в чате", blank=True, null=True,default=0)
#     sum_bal = models.IntegerField("Баллы", blank=True, null=True, default=0)    
#     groups = models.ManyToManyField(Group, verbose_name='Groups', blank=True, related_name='custom_user_set',)    
#     user_permissions = models.ManyToManyField(Permission, verbose_name='User permissions', blank=True, related_name='custom_user_set_permissions',)    
#     date_of_registration = models.DateField(auto_now_add=True, verbose_name='дата регистрации')
#     def save(self, *args, **kwargs):
#         if self.birthday:today == date.today():
#             age = today.year - self.birthday.year-((today.month, today.day) < (self.birthday.month, self.birthday.day))
#             self.age = age    
#         super().save(*args, **kwargs)

#     class Meta:        
#         verbose_name = "Пользователь"
#         verbose_name_plural = "Пользователи"