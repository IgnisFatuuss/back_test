# Generated by Django 4.2.5 on 2023-10-11 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Profile", "0008_alter_profile_default_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="adress",
            name="default",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
