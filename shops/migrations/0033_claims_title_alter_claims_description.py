# Generated by Django 4.2.5 on 2023-10-26 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shops", "0032_claims_remove_storesreviews_store_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="claims",
            name="title",
            field=models.CharField(
                default=False, max_length=255, verbose_name="Заголовок"
            ),
        ),
        migrations.AlterField(
            model_name="claims",
            name="description",
            field=models.CharField(max_length=255, verbose_name="Описание"),
        ),
    ]