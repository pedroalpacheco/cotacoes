# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-08 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dolar',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('compra', models.TextField(blank=True, null=True)),
                ('venda', models.TextField(blank=True, null=True)),
                ('data', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dolar',
                'managed': False,
            },
        ),
    ]
