# Generated by Django 5.0.2 on 2024-02-22 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reply', '0002_remove_reply_reply_groupnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='group_id',
            field=models.BigIntegerField(null=True),
        ),
    ]
