# Generated by Django 5.0.2 on 2024-02-27 08:58

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'base_manager_name': 'sell_price_objects'},
        ),
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('sell_price_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
