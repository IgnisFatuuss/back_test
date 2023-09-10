# Generated by Django 4.2.5 on 2023-09-10 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Stopwords",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=120, verbose_name="Стоп слова")),
            ],
            options={
                "verbose_name": "Стоп слово",
                "verbose_name_plural": "Стоп слова",
            },
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True, verbose_name="Дата")),
                (
                    "last_update",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Последнее обновление"
                    ),
                ),
                ("subject", models.CharField(max_length=255, verbose_name="Предмет")),
                (
                    "description",
                    models.TextField(
                        help_text="Подробное описание вашей проблемы.",
                        verbose_name="Описание",
                    ),
                ),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[
                            (0, "Новое"),
                            (1, "Обратная связь"),
                            (3, "в процессе"),
                            (4, "Решенный"),
                            (5, "Закрытый"),
                        ],
                        default=0,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "type",
                    models.SmallIntegerField(
                        choices=[(0, "Обычное"), (1, "Жалоба"), (3, "С темой")],
                        default=0,
                        verbose_name="Тип",
                    ),
                ),
                ("html_content", models.TextField(verbose_name="Объект")),
                (
                    "assignee",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assigned_tickets",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Правопреемник",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tickets",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Создатель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Тикет",
                "verbose_name_plural": "Тикеты",
                "ordering": ["date"],
            },
        ),
        migrations.CreateModel(
            name="TicketComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True, verbose_name="Дата")),
                ("comment", models.TextField(verbose_name="Комментарий")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                (
                    "ticket",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="moderation.ticket",
                        verbose_name="Ticket",
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий тикета",
                "verbose_name_plural": "Комментарии тикета",
                "ordering": ["date"],
            },
        ),
    ]
