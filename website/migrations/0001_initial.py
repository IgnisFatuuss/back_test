# Generated by Django 4.2.5 on 2023-09-10 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import faicon.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Blogs",
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
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
            },
        ),
        migrations.CreateModel(
            name="Faq",
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
                    "question",
                    models.CharField(max_length=500, null=True, verbose_name="Вопрос"),
                ),
                (
                    "answer",
                    models.TextField(max_length=500, null=True, verbose_name="Ответ"),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=160, unique=True, verbose_name="Ссылка"
                    ),
                ),
            ],
            options={
                "verbose_name": "Часто задаваемый вопрос",
                "verbose_name_plural": "Часто задаваемые вопросы",
            },
        ),
        migrations.CreateModel(
            name="GeneralSettings",
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
                    "logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="Логотип"
                    ),
                ),
                (
                    "favicon",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="Фавикон"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="Название"
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        blank=True, max_length=500, null=True, verbose_name="Контент"
                    ),
                ),
                (
                    "pn_pt",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="ПН-ПТ"
                    ),
                ),
                (
                    "sb",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="СБ"
                    ),
                ),
                (
                    "vs",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="ВС"
                    ),
                ),
            ],
            options={
                "verbose_name": "Общая настройка",
                "verbose_name_plural": "Общие настройки",
            },
        ),
        migrations.CreateModel(
            name="Pages",
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
                "verbose_name": "Страница",
                "verbose_name_plural": "Страницы",
            },
        ),
        migrations.CreateModel(
            name="Regions",
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
                    "image",
                    models.ImageField(
                        upload_to="regions/images/", verbose_name="Изображение"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=500, null=True, verbose_name="Название"
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
                "verbose_name": "Регион",
                "verbose_name_plural": "Регионы",
            },
        ),
        migrations.CreateModel(
            name="Tags",
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
                    "image",
                    models.ImageField(
                        upload_to="tags/images/", verbose_name="Изображение"
                    ),
                ),
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
                    "slug",
                    models.SlugField(
                        max_length=160, unique=True, verbose_name="Ссылка"
                    ),
                ),
            ],
            options={
                "verbose_name": "Метка",
                "verbose_name_plural": "Метки",
            },
        ),
        migrations.CreateModel(
            name="Social",
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
                    "link",
                    models.SlugField(max_length=500, null=True, verbose_name="Ссылка"),
                ),
                ("icon", faicon.fields.FAIconField(max_length=50)),
                (
                    "general_settings",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="website.generalsettings",
                        verbose_name="Настройки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Социальная сеть",
                "verbose_name_plural": "Социальные сети",
            },
        ),
        migrations.CreateModel(
            name="Rubric",
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
                    "image",
                    models.ImageField(
                        upload_to="categories/images/", verbose_name="Изображение"
                    ),
                ),
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
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="website.rubric",
                        verbose_name="Родитель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Phones",
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
                    "phone",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="Телефон"
                    ),
                ),
                (
                    "generalsettings",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="website.generalsettings",
                        verbose_name="Настройки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Телефон",
                "verbose_name_plural": "Телефоны",
            },
        ),
        migrations.CreateModel(
            name="Contacts",
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
                    "general_settings",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="website.generalsettings",
                        verbose_name="Настройки",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="website.regions",
                        verbose_name="Настройки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Контакт",
                "verbose_name_plural": "Контакты",
            },
        ),
        migrations.CreateModel(
            name="Commentaries",
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
                    "content",
                    models.TextField(max_length=500, null=True, verbose_name="Контент"),
                ),
                (
                    "blogs",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="website.blogs",
                        verbose_name="Категория",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="channel",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий",
                "verbose_name_plural": "Комментарии",
            },
        ),
        migrations.AddField(
            model_name="blogs",
            name="rubric",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="website.rubric",
                verbose_name="Категория",
            ),
        ),
        migrations.AddField(
            model_name="blogs",
            name="tags",
            field=models.ManyToManyField(
                blank=True, to="website.tags", verbose_name="Метки"
            ),
        ),
    ]