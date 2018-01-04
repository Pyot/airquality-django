# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-31 09:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airpollution', '0005_auto_20170830_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pollution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('pm25', models.FloatField()),
                ('pm10', models.FloatField()),
                ('o3', models.FloatField()),
                ('no2', models.FloatField()),
                ('so2', models.FloatField()),
                ('nh3', models.FloatField()),
                ('pb', models.FloatField()),
                ('aqi', models.FloatField()),
                ('station_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airpollution.Station')),
            ],
        ),
    ]
