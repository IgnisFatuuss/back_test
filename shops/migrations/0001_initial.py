# Generated by Django 4.2.5 on 2023-09-15 15:04

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
            name="Attributs",
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
                ("name", models.CharField(max_length=255, verbose_name="Имя")),
            ],
            options={
                "verbose_name": "Атрибут",
                "verbose_name_plural": "Атрибуты",
            },
        ),
        migrations.CreateModel(
            name="Brands",
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
                ("name", models.CharField(max_length=255, verbose_name="Имя")),
                (
                    "slug",
                    models.SlugField(max_length=200, unique=True, verbose_name="URL"),
                ),
                (
                    "logo",
                    models.ImageField(
                        upload_to="shops/brands/", verbose_name="Логотип"
                    ),
                ),
            ],
            options={
                "verbose_name": "Брэнд",
                "verbose_name_plural": "Брэнды",
            },
        ),
        migrations.CreateModel(
            name="Categories",
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
                ("name", models.CharField(max_length=255, verbose_name="Имя")),
                (
                    "slug",
                    models.SlugField(max_length=200, unique=True, verbose_name="URL"),
                ),
                (
                    "img",
                    models.ImageField(
                        upload_to="shops/categories/", verbose_name="Изображение"
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="child",
                        to="shops.categories",
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
            name="Products",
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
                ("name", models.CharField(max_length=250, verbose_name="Имя")),
                ("article", models.CharField(max_length=250, verbose_name="Артикль")),
                ("slug", models.SlugField(unique=True, verbose_name="URL")),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "available",
                    models.BooleanField(default=True, verbose_name="Доступность"),
                ),
                (
                    "create",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создано"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now_add=True, verbose_name="Обновлено"),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="shops.brands",
                        verbose_name="Брэнд",
                    ),
                ),
                (
                    "category",
                    models.ManyToManyField(
                        related_name="categories",
                        to="shops.categories",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
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
                ("name", models.CharField(max_length=255, verbose_name="Имя")),
                (
                    "slug",
                    models.SlugField(max_length=200, unique=True, verbose_name="URL"),
                ),
            ],
            options={
                "verbose_name": "Тэг",
                "verbose_name_plural": "Тэги",
            },
        ),
        migrations.CreateModel(
            name="Variations",
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
                    "status",
                    models.PositiveIntegerField(
                        blank=True,
                        choices=[(1, "Выбор"), (2, "Цифры")],
                        default=1,
                        null=True,
                        verbose_name="Статус",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Имя")),
                (
                    "participate",
                    models.BooleanField(
                        blank=True, null=True, verbose_name="Участвовать в варицациях"
                    ),
                ),
            ],
            options={
                "verbose_name": "Вариация",
                "verbose_name_plural": "Вариации",
            },
        ),
        migrations.CreateModel(
            name="VariationProducts",
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
                ("price", models.PositiveIntegerField(verbose_name="Цена")),
                (
                    "attributs",
                    models.ManyToManyField(
                        to="shops.attributs", verbose_name="Аттрибуты"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="shops.products",
                        verbose_name="Товар",
                    ),
                ),
            ],
            options={
                "verbose_name": "Вариация продуктов",
                "verbose_name_plural": "Вариации продуктов",
            },
        ),
        migrations.CreateModel(
            name="Reviews",
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
                ("date", models.DateField(auto_now=True, verbose_name="Дата")),
                ("text", models.TextField(verbose_name="Текст")),
                ("review", models.PositiveIntegerField(verbose_name="Отзыв")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="reviews",
                        to="shops.products",
                        verbose_name="Продукт",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Отзывы",
                "verbose_name_plural": "Отзывы",
            },
        ),
        migrations.AddField(
            model_name="products",
            name="tag",
            field=models.ManyToManyField(
                related_name="tags", to="shops.tags", verbose_name="Тэг"
            ),
        ),
        migrations.CreateModel(
            name="Orders",
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
                    "status",
                    models.PositiveIntegerField(
                        blank=True,
                        choices=[(1, "Не оплачено"), (2, "Оплачено")],
                        default=1,
                        null=True,
                        verbose_name="Статус",
                    ),
                ),
                ("order_sum", models.PositiveIntegerField(verbose_name="Общая сумма")),
                ("date", models.DateField(auto_now=True, verbose_name="Дата")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "variation",
                    models.ManyToManyField(
                        to="shops.variations", verbose_name="Вариация"
                    ),
                ),
            ],
            options={
                "verbose_name": "Заказ",
                "verbose_name_plural": "Заказы",
            },
        ),
        migrations.CreateModel(
            name="Gallereis",
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
                    models.ImageField(upload_to="shops/", verbose_name="Картинка"),
                ),
                (
                    "variations",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="gallereis",
                        to="shops.variationproducts",
                        verbose_name="Вариация",
                    ),
                ),
            ],
            options={
                "verbose_name": "Галлерея",
                "verbose_name_plural": "Галлереи",
            },
        ),
        migrations.CreateModel(
            name="Faqs",
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
                ("answer", models.TextField(verbose_name="Ответ")),
                ("question", models.TextField(verbose_name="Вопрос")),
                ("date", models.DateField(auto_now=True, verbose_name="Дата")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="shops.products",
                        verbose_name="Продукт",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Часто задаваемые вопросы",
                "verbose_name_plural": "Часто задаваемые вопросы",
            },
        ),
        migrations.CreateModel(
            name="Emotions",
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
                    "rate",
                    models.CharField(
                        choices=[("2", "Дизлайк"), ("1", "Лайк")],
                        max_length=255,
                        verbose_name="Оценка",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="shops.products",
                        verbose_name="Продукт",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Эмоция",
                "verbose_name_plural": "Эмоции",
            },
        ),
        migrations.CreateModel(
            name="Cards",
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
                ("order_sum", models.PositiveIntegerField(verbose_name="Общая сумма")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "variation",
                    models.ManyToManyField(
                        to="shops.variations", verbose_name="Вариации"
                    ),
                ),
            ],
            options={
                "verbose_name": "Корзина",
                "verbose_name_plural": "Корзины",
            },
        ),
        migrations.AddField(
            model_name="attributs",
            name="variation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="shops.variations",
                verbose_name="Вариации",
            ),
        ),
    ]
