# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-23 02:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myTodo', '0014_auto_20171022_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 23, 2, 2, 39, 96182, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='todo',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
