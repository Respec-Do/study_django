# Generated by Django 5.0.2 on 2024-03-14 16:16

import django.db.models.deletion
import django.views.generic.base
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomVisitCountMixin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_count', models.PositiveIntegerField(default=0, help_text='Visit count')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VisitRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MainView',
            fields=[
                ('customvisitcountmixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.customvisitcountmixin')),
            ],
            options={
                'abstract': False,
            },
            bases=('main.customvisitcountmixin', django.views.generic.base.View),
        ),
    ]
