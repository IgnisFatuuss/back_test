# Generated by Django 4.2.5 on 2023-10-20 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shops", "0028_alter_stores_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="stores",
            name="image",
            field=models.ImageField(
                default=False, upload_to="shops/stores", verbose_name="Картинка"
            ),
        ),
    ]