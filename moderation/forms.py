from django import forms
from .models import *


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('subject', 'description', 'html_content')