# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-31 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airpollution', '0007_auto_20170831_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollution',
            name='humdity',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='pollution',
            name='pressure',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='pollution',
            name='temp',
            field=models.FloatField(default=0),
        ),
    ]
