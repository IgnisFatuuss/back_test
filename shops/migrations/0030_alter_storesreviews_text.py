# Generated by Django 4.2.5 on 2023-10-20 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shops", "0029_stores_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="storesreviews",
            name="text",
            field=models.CharField(default=False, max_length=255, verbose_name="Текст"),
        ),
    ]
