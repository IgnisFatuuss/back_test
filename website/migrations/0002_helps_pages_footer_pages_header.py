# Generated by Django 4.2.5 on 2023-10-15 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Helps",
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
                ("data", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        max_length=500, null=True, verbose_name="Название"
                    ),
                ),
                (
                    "content",
                    models.TextField(max_length=500, null=True, verbose_name="Контент"),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=500, null=True, verbose_name="Заголовок"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        max_length=500, null=True, verbose_name="Описание"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=160, unique=True, verbose_name="Ссылка"
                    ),
                ),
            ],
            options={
                "verbose_name": "Руководство",
                "verbose_name_plural": "Руководство",
            },
        ),
        migrations.AddField(
            model_name="pages",
            name="footer",
            field=models.BooleanField(default=False, verbose_name="Подвал"),
        ),
        migrations.AddField(
            model_name="pages",
            name="header",
            field=models.BooleanField(default=False, verbose_name="Шапка"),
        ),
    ]