# from django import forms
# from django import forms
# from .models import User
# from django.contrib.auth.forms import UserCreationForm
# from captcha.fields import ReCaptchaField
# from django.forms import ClearableFileInput

from django import forms
from .models import Profile, Adress


class ProfileForm(forms.ModelForm):
    birthday = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Profile
        fields = ('avatar', 'birthday', 'city', 'zip_code', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Добавьте виджеты и атрибуты для каждого поля
        self.fields['avatar'].widget = forms.FileInput(attrs={
            'class': 'form-control',
            'type': 'file',
            'placeholder': 'Аватар',
        })
        self.fields['city'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'Город',
        })
        self.fields['zip_code'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'Почтовый индекс',
        })
        self.fields['phone'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'Телефон',
        })

        self.fields['birthday'].label = 'Дата рождения'

class AdressEditForm(forms.ModelForm):

    class Meta:
        model = Adress
        fields = ('country', 'first_name', 'last_name', 'company_name', 'city', 'street', 'postcode', 'appartament', 'email', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['country'].widget = forms.Select(attrs={
        #     'placeholder': 'Выберите страну',
        #     'class': 'form-control form-control-select2',
        # })
        self.fields['first_name'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Имя',
            'type': 'text',  # Добавляем type="text"
        })
        self.fields['last_name'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Фамилия',
            'type': 'text',  # Добавляем type="text"
        })
        self.fields['company_name'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Имя компании',
            'type': 'text',  # Добавляем type="text"
        })
        self.fields['city'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Город',
            'type': 'text',  # Добавляем type="text"
        })
        self.fields['street'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Улица',
            'type': 'text',  # Добавляем type="text"
        })
        self.fields['postcode'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Почтовый код',
            'type': 'text',  # Добавляем type="text"
        })
        self.fields['appartament'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Апартаменты',
            'type': 'text',  # Добавляем type="text"
        })
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'type': 'text',  # Добавляем type="text"
        })
        self.fields['phone'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Телефон',
            'type': 'text',  # Добавляем type="text"
        })
# class LoginForm(forms.Form):
#     username = forms.CharField(label="Ник на сайте", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'username'}))
#     password = forms.CharField(label="Пароль", widget=forms.PasswordInput())

# class UserProfileForm(forms.ModelForm):
#     avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'account__file'}))

#     class Meta:
#         model = User
#         fields = ['avatar', 'birthday', 'age', 'gender', 'username', 'email', 'time_zone']


# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True, label='Email')  # Добавьте поле для Email
#     username = forms.CharField(required=True, label='Имя')  # Добавьте поле для Email
#     birthday = forms.DateField(required=False, label='Дата рождения', widget=forms.DateInput(attrs={'id': 'datepicker'}))
#     recaptcha = ReCaptchaField()

#     class Meta:
#         model = User  # Укажите модель пользователя, обычно 'User'
#         fields = ('username', 'email', 'password1', 'password2', 'gender', 'birthday')  # Поля, которые будут отображаться в форме