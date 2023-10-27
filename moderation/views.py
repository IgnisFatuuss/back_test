from django.shortcuts import render
from django.db import transaction
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import ListView, DetailView, TemplateView, View
from .models import *
from .forms import *
# Create your views here.

class SupportView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'tickets': Ticket.objects.all(),
            'form' : TicketForm
        }

        return render(request, 'moderation/support.html', context)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = TicketForm(request.POST or None)
        if form.is_valid():
            new_ticket = form.save(commit=False)
            for field, value in form.cleaned_data.items():
                setattr(new_ticket, field, value)
            new_ticket.creator = self.request.user
            new_ticket.save()  # Сохраните объект профиля
            return HttpResponseRedirect('/account/dashboard')  # Перенаправить пользователя на страницу профиля после успешного сохранения
        return HttpResponseRedirect('/account/dashboard')