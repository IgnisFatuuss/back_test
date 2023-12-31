# Generated by Django 4.2.5 on 2023-09-28 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shops", "0004_carts"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carts",
            name="for_anonymous",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="carts",
            name="in_order",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="CartProduct",
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
                ("qty", models.PositiveIntegerField(default=1)),
                (
                    "final_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=9, verbose_name="Общая цена"
                    ),
                ),
                (
                    "card",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_products",
                        to="shops.carts",
                        verbose_name="Kорзина",
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
        ),
        migrations.AlterField(
            model_name="carts",
            name="products",
            field=models.ManyToManyField(
                blank=True,
                related_name="cart",
                to="shops.cartproduct",
                verbose_name="Продукты",
            ),
        ),
    ]
