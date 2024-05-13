# Generated by Django 4.2.11 on 2024-05-03 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0006_remove_menuitem_menu_alter_menuitem_parent_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menuitem",
            name="parent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tags",
                to="menu.menu",
            ),
        ),
    ]
