from django import forms
from .models import Orders, Reviews, Faqs
from django import forms
from .models import User



class OrderForm(forms.ModelForm):
    # order_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = Orders
        fields = ('first_name', 'last_name', 'company_name', 'country', 'city', 'street', 'postcode', 'appartament', 'email', 'phone', 'notes',)
    
    widgets = {
        'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
        'country': forms.Select(attrs={'class': 'form-control form-control-select2'}),
        'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Town / City'}),
        'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Address'}),
        'postcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postcode / ZIP'}),
        'appartament': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apartment, suite, unit etc.'}),
        'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}),
        'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
        'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Order notes (Optional)', 'rows': '4'}),
    }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('text', 'review',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['review'].widget.attrs.update({'class': 'form-control'})
        self.fields['review'].widget.attrs.update({'rows': 1})

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Faqs
        fields = ('question',)
    
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Faqs
        fields = ('answer',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['answer'].widget = forms.TextInput(attrs={ 'class': 'form-control', 'type': 'text'})

