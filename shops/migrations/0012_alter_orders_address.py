# Generated by Django 4.2.5 on 2023-10-12 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Profile", "0011_remove_profile_default_address"),
        ("shops", "0011_remove_orders_appartament_remove_orders_city_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orders",
            name="address",
            field=models.ForeignKey(
                default=False,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="address",
                to="Profile.adress",
                verbose_name="Адрес",
            ),
        ),
    ]
