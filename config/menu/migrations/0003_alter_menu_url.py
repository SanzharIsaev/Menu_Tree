# Generated by Django 4.2.11 on 2024-05-02 12:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0002_alter_menu_parent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="url",
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]