# Generated by Django 5.0.2 on 2024-03-14 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitrecord',
            name='id',
        ),
        migrations.AlterField(
            model_name='visitrecord',
            name='date',
            field=models.DateField(primary_key=True, serialize=False),
        ),
    ]