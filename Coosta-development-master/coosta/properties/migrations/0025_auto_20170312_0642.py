# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-12 06:17
from __future__ import unicode_literals

from django.db import migrations


def load_property_status(apps, schema_editor):
    Status = apps.get_model('properties', 'PropertyStatus')
    status = Status(id=1, status='edit')
    status.save()
    status = Status(id=2, status='get_valuation')
    status.save()
    status = Status(id=3, status='published')
    status.save()
    status = Status(id=4, status='offers')
    status.save()
    status = Status(id=5, status='sign_contract')
    status.save()
    status = Status(id=6, status='escrow')
    status.save()


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0024_propertystatus'),
    ]

    operations = [
        migrations.RunPython(load_property_status),
    ]
