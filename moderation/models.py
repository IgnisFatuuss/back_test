from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class Ticket(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Создатель", on_delete=models.CASCADE, related_name='tickets')
    date = models.DateTimeField(verbose_name="Дата", auto_now_add=True)
    last_update = models.DateTimeField(verbose_name="Последнее обновление", auto_now=True)
    subject = models.CharField(verbose_name="Предмет", max_length=255)
    description = models.TextField(verbose_name="Описание", help_text=_("Подробное описание вашей проблемы."))
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Правопреемник", on_delete=models.CASCADE, related_name="assigned_tickets", blank=True, null=True)
    STATUS_CHOICES = [
        (0, _("Новое")),
        (1, _("Обратная связь")),
        (3, _("в процессе")),
        (4, _("Решенный")),
        (5, _("Закрытый")),
    ]
    status = models.SmallIntegerField(verbose_name="Статус", choices=STATUS_CHOICES, default=0)
    STATUS_TYPE = [
        (0, _("Обычное")),
        (1, _("Жалоба")),
        (3, _("С темой")),
    ]
    type = models.SmallIntegerField(verbose_name="Тип", choices=STATUS_TYPE, default=0)
    CLOSED_STATUSES = getattr(settings, 'TICKETS_CLOSED_STATUSES', (4, 5))
    html_content = models.TextField(verbose_name="Объект")



    class Meta:
        verbose_name = "Тикет"
        verbose_name_plural = "Тикеты"
        ordering = ['date']


    def get_comments_count(self):
        return self.comments.count()

    def get_latest_comment(self):
        return self.comments.latest('date')

    def __str__(self):
        return "%s# %s" % (self.id, self.subject)

    def is_closed(self):
        return self.status in self.CLOSED_STATUSES

    def is_answered(self):
        try:
            latest = self.get_latest_comment()
        except TicketComment.DoesNotExist:
            return False
        return latest.author != self.creator
    is_answered.boolean = True
    is_answered.short_description = _("Is answered")


class TicketComment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, verbose_name=_("Ticket"), related_name='comments')
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")
    comment = models.TextField(verbose_name="Комментарий")

    class Meta:
        verbose_name = _("Комментарий тикета")
        verbose_name_plural = _("Комментарии тикета")
        ordering = ['date']

    def __str__(self):
        return "Comment on " + str(self.ticket)

class Stopwords(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Стоп слова", max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Стоп слово"
        verbose_name_plural = "Стоп слова"