# Generated by Django 4.2.5 on 2023-10-12 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Profile", "0010_remove_histories_product"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="default_address",
        ),
    ]
