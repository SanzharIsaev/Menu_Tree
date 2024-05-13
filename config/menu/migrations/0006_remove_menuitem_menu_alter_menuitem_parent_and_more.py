# Generated by Django 4.2.11 on 2024-05-03 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0005_alter_menu_options_alter_menuitem_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menuitem",
            name="menu",
        ),
        migrations.AlterField(
            model_name="menuitem",
            name="parent",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="menu_items",
                to="menu.menu",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="menuitem",
            name="url",
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]