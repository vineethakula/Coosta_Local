# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-05 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0017_auto_20170116_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ZIPcode', models.TextField(blank=True, null=True)),
                ('TaxRateArea_CITY', models.TextField(blank=True, null=True)),
                ('AIN', models.IntegerField(blank=True, null=True)),
                ('RollYear', models.IntegerField(blank=True, null=True)),
                ('TaxRateArea', models.TextField(blank=True, null=True)),
                ('AssessorID', models.TextField(blank=True, null=True)),
                ('PropertyLocation', models.TextField(blank=True, null=True)),
                ('PropertyType', models.TextField(blank=True, null=True)),
                ('PropertyUseCode', models.TextField(blank=True, null=True)),
                ('GeneralUseType', models.TextField(blank=True, null=True)),
                ('SpecificUseType', models.TextField(blank=True, null=True)),
                ('SpecificUseDetail1', models.TextField(blank=True, null=True)),
                ('SpecificUseDetail2', models.TextField(blank=True, null=True)),
                ('totBuildingDataLines', models.IntegerField(blank=True, null=True)),
                ('YearBuilt', models.IntegerField(blank=True, null=True)),
                ('EffectiveYearBuilt', models.IntegerField(blank=True, null=True)),
                ('SQFTmain', models.IntegerField(blank=True, null=True)),
                ('Bedrooms', models.IntegerField(blank=True, null=True)),
                ('Bathrooms', models.IntegerField(blank=True, null=True)),
                ('Units', models.IntegerField(blank=True, null=True)),
                ('RecordingDate', models.TextField(blank=True, null=True)),
                ('LandValue', models.IntegerField(blank=True, null=True)),
                ('LandBaseYear', models.IntegerField(blank=True, null=True)),
                ('ImprovementValue', models.IntegerField(blank=True, null=True)),
                ('ImpBaseYear', models.IntegerField(blank=True, null=True)),
                ('TotalLandImpValue', models.IntegerField(blank=True, null=True)),
                ('HomeownersExemption', models.IntegerField(blank=True, null=True)),
                ('RealEstateExemption', models.IntegerField(blank=True, null=True)),
                ('FixtureValue', models.IntegerField(blank=True, null=True)),
                ('FixtureExemption', models.IntegerField(blank=True, null=True)),
                ('PersonalPropertyValue', models.IntegerField(blank=True, null=True)),
                ('PersonalPropertyExemption', models.IntegerField(blank=True, null=True)),
                ('isTaxableParcel', models.TextField(blank=True, null=True)),
                ('TotalValue', models.IntegerField(blank=True, null=True)),
                ('TotalExemption', models.IntegerField(blank=True, null=True)),
                ('netTaxableValue', models.IntegerField(blank=True, null=True)),
                ('SpecialParcelClassification', models.TextField(blank=True, null=True)),
                ('AdministrativeRegion', models.TextField(blank=True, null=True)),
                ('Cluster', models.TextField(blank=True, null=True)),
                ('ParcelBoundaryDescription', models.TextField(blank=True, null=True)),
                ('HouseNo', models.IntegerField(blank=True, null=True)),
                ('HouseFraction', models.TextField(blank=True, null=True)),
                ('StreetDirection', models.TextField(blank=True, null=True)),
                ('StreetName', models.TextField(blank=True, null=True)),
                ('UnitNo', models.TextField(blank=True, null=True)),
                ('City', models.TextField(blank=True, null=True)),
                ('ZIPcode5', models.IntegerField(blank=True, null=True)),
                ('rowID', models.TextField(blank=True, null=True)),
                ('CENTER_LAT', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
                ('CENTER_LON', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
            ],
            options={
                'verbose_name_plural': 'Parcel',
            },
        ),
    ]