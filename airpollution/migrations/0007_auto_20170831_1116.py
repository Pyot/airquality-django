# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-31 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airpollution', '0006_pollution'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollution',
            name='humdity',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='pollution',
            name='pressure',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='pollution',
            name='temp',
            field=models.FloatField(null=True),
        ),
    ]
