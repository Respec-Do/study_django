# Generated by Django 5.0.2 on 2024-03-14 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0006_exhibition_exhibition_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibition',
            name='exhibition_view_count',
            field=models.IntegerField(default=0),
        ),
    ]
