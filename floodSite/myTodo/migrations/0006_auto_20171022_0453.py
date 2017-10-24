# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-22 04:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myTodo', '0005_auto_20171022_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(verbose_name=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 22, 4, 53, 59, 145581, tzinfo=utc)),
        ),
    ]