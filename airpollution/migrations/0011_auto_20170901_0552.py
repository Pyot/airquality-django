# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-01 05:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airpollution', '0010_auto_20170831_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pollution',
            old_name='humdity',
            new_name='h',
        ),
        migrations.RenameField(
            model_name='pollution',
            old_name='pressure',
            new_name='p',
        ),
        migrations.RenameField(
            model_name='pollution',
            old_name='temp',
            new_name='t',
        ),
    ]
