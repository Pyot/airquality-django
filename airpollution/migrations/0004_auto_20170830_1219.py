# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-30 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airpollution', '0003_auto_20170830_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='uid',
            field=models.IntegerField(unique=True),
        ),
    ]