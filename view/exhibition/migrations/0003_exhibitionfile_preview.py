# Generated by Django 5.0.2 on 2024-03-05 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0002_exhibition_exhibition_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibitionfile',
            name='preview',
            field=models.BooleanField(default=False),
        ),
    ]