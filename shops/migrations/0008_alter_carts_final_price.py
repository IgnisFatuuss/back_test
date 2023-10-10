# Generated by Django 4.2.5 on 2023-10-02 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shops", "0007_remove_orders_variation_orders_appartament_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carts",
            name="final_price",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=9, verbose_name="Цена"
            ),
        ),
    ]
