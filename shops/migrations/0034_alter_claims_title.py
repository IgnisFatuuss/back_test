# Generated by Django 4.2.5 on 2023-10-26 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shops", "0033_claims_title_alter_claims_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="claims",
            name="title",
            field=models.CharField(max_length=255, verbose_name="Заголовок"),
        ),
    ]
