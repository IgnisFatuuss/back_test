# Generated by Django 4.2.5 on 2023-10-26 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shops", "0034_alter_claims_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="claims",
            name="image",
            field=models.ImageField(
                blank=True, upload_to="shops/claims", verbose_name="Картинка"
            ),
        ),
    ]