# Generated by Django 4.2.5 on 2023-10-10 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Profile", "0002_remove_profile_address_adress"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="adress",
            options={"verbose_name": "Адрес", "verbose_name_plural": "Адресы"},
        ),
        migrations.AddField(
            model_name="profile",
            name="default_address",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="Profile.adress",
                verbose_name="Стандартный адрес",
            ),
            preserve_default=False,
        ),
    ]
