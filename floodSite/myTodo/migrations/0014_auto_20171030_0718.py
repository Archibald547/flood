# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 07:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myTodo', '0013_auto_20171028_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 30, 7, 18, 18, 849410, tzinfo=utc)),
        ),
    ]
