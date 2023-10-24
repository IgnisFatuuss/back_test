# Generated by Django 4.2.5 on 2023-10-20 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shops", "0027_stores_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stores",
            name="slug",
            field=models.SlugField(max_length=200, unique=True, verbose_name="URL"),
        ),
    ]
