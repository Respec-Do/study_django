# Generated by Django 5.0.2 on 2024-03-14 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_member_member_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='member_is_school',
            field=models.BooleanField(default=False),
        ),
    ]
