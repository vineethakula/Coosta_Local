# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-14 07:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0025_auto_20170312_0642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='status',
        ),
    ]
