# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-13 15:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name=b'Name of Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="Person's name")),
                ('address', models.CharField(max_length=255)),
                ('info', models.TextField(verbose_name=b'Info on Person')),
                ('born', models.DateTimeField(default=datetime.datetime(2001, 1, 1, 1, 1))),
                ('hobby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djqscsv_tests.Activity')),
            ],
        ),
    ]
