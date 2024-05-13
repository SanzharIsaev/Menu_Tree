# Generated by Django 4.2.11 on 2024-05-06 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0011_menu_parent_delete_menuitem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tags",
                to="menu.menu",
                verbose_name="Родитель",
            ),
        ),
    ]
