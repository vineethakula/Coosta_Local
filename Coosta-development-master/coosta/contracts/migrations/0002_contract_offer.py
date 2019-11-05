# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-17 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0002_offers_accepted'),
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='offer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='offers.Offers'),
        ),
    ]
