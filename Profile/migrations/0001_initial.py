# Generated by Django 4.2.5 on 2023-09-15 15:04

import Profile.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("shops", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        default="default/profile/profile-thumb.jpg",
                        upload_to=Profile.models.get_user_dir,
                        verbose_name="Аватар",
                    ),
                ),
                (
                    "birthday",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата рождения"
                    ),
                ),
                (
                    "address",
                    models.CharField(blank=True, max_length=100, verbose_name="Адресс"),
                ),
                (
                    "city",
                    models.CharField(blank=True, max_length=100, verbose_name="Город"),
                ),
                (
                    "zip_code",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Почтовый индекс"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="Телефон"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Профиль",
                "verbose_name_plural": "Профили",
            },
        ),
        migrations.CreateModel(
            name="Histories",
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
                ("url", models.URLField(verbose_name="Ссылка")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shops.products",
                        verbose_name="Продукт",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Profile.profile",
                        verbose_name="Профиль",
                    ),
                ),
            ],
            options={
                "verbose_name": "История",
                "verbose_name_plural": "Истории",
            },
        ),
    ]
