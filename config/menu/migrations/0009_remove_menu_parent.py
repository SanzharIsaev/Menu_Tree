# Generated by Django 4.2.11 on 2024-05-06 13:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0008_menu_parent_delete_menuitem"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menu",
            name="parent",
        ),
    ]
