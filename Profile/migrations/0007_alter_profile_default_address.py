# Generated by Django 4.2.5 on 2023-10-10 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Profile", "0006_profile_default_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="default_address",
            field=models.ForeignKey(
                blank=True,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="Profile.adress",
                verbose_name="Стандартный адрес",
            ),
        ),
    ]
