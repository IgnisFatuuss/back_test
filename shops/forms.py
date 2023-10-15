from django import forms
from .models import Orders, Reviews, Faqs
from django import forms
from .models import User



class OrderForm(forms.ModelForm):
    # order_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = Orders
        fields = ('notes',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['notes'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Примечания',
            'rows': '4',
        })

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

