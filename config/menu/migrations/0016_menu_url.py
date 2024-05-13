# Generated by Django 4.2.11 on 2024-05-08 08:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0015_alter_menu_parent"),
    ]

    operations = [
        migrations.AddField(
            model_name="menu",
            name="url",
            field=models.SlugField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
