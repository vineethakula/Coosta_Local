# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-16 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0016_auto_20170106_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='basement',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='car_park',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='home_type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='state',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
