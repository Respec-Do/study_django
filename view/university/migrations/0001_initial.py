# Generated by Django 5.0.2 on 2024-03-14 03:58

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0003_member_member_phone_member_member_school_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('university_member_school', models.CharField(max_length=100)),
                ('university_member_major', models.CharField(max_length=100)),
                ('university_member_points', models.BigIntegerField(default=0)),
                ('university_member_birth', models.DateField(default='2005-01-01')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.member')),
            ],
            options={
                'db_table': 'tbl_university',
                'ordering': ['-id'],
            },
        ),
    ]
