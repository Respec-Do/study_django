# Generated by Django 5.0.2 on 2024-02-23 09:51

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0002_member_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('payment', models.TextField()),
                ('price', models.BigIntegerField()),
                ('delivery_address', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.member')),
            ],
            options={
                'db_table': 'tbl_order',
                'ordering': ['-id'],
            },
        ),
    ]
