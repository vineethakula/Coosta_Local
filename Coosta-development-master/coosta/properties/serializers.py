from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
import os
from coosta_users.serializers import UserSerializer
from statistic.models import PageView
from offers.models import Offers


class ImagesSerializer(serializers.HyperlinkedModelSerializer):

    image = serializers.ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Images
        fields = ('url', 'id', 'image')


class GetPropertyImagesSerializer(serializers.HyperlinkedModelSerializer):

    image = ImagesSerializer(read_only=True, required=False)

    class Meta:
        model = PropertyImages
        fields = ('url', 'id', 'image', 'property')


class PostPropertyImagesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PropertyImages
        fields = ('url', 'id', 'image', 'property')


class PropertyStatusSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PropertyStatus
        fields = ('id', 'status')


class GetPropertySerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()
    images = ImagesSerializer(many=True)
    status = PropertyStatusSerializer()
    page_view = serializers.SerializerMethodField('page_view_count')
    highest_offer = serializers.SerializerMethodField('highest_offer_count')
    total_offer = serializers.SerializerMethodField('total_offer_count')

    def page_view_count(self, property):
        return PageView.objects.filter(property__id=property.id).count()

    def highest_offer_count(self, property):
        offers = Offers.objects.filter(property__id=property.id).order_by('-highest_offer_amount')
        if offers:
            return offers[0].highest_offer_amount
        else:
            return 0

    def total_offer_count(self, property):
        return Offers.objects.filter(property__id=property.id).count()

    class Meta:
        model = Property
        fields = ('url', 'id', 'user', 'address', 'city', 'state', 'zip_code', 'home_type', 'beds', 'property_title',
                  'property_value', 'baths', 'images', 'rooms', 'property_size', 'floors', 'roof', 'basement', 'year_built',
                  'description', 'other_features', 'status', 'latitude', 'longitude', 'year_renovated',
                  'car_park', 'listed_on', 'search_index', 'thumbnail', 'completed', 'active', 'page_view',
                  'highest_offer', 'total_offer')


class PostPropertySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Property
        fields = ('url', 'id', 'user', 'address', 'city', 'state', 'zip_code', 'home_type', 'beds', 'property_title',
                  'property_value', 'baths', 'images', 'rooms', 'property_size', 'floors', 'roof', 'basement', 'year_built',
                  'description', 'other_features', 'status', 'latitude', 'longitude', 'year_renovated',
                  'car_park', 'search_index', 'thumbnail', 'completed', 'active')

    def create(self, validated_data):
        try:
            validated_data['search_index'] = validated_data.get('address') + ", " + validated_data.get('city') \
                                             + ", " + validated_data.get('state') + " " + validated_data.get('zip_code')
            validated_data['search_index'] = " ".join(validated_data['search_index'].split())
        except:
            pass
        p = Property(**validated_data)
        p.save()
        return p

    def update(self, instance, validated_data):
        try:
            p = Property(id=instance.id, **validated_data)
            p.search_index = validated_data.get('address') + ", " + validated_data.get('city') \
                             + ", " + validated_data.get('state') + " " + validated_data.get('zip_code')
            p.search_index = " ".join(p.search_index.split())
            p.save()
        except:
            pass
        return p


class GetShortListedPropertySerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer(read_only=True)
    property = GetPropertySerializer()

    class Meta:
        model = ShortListedProperty
        fields = ('url', 'id', 'user', 'property', 'shortlisted_on')


class PostShortListedPropertySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ShortListedProperty
        fields = ('url', 'id', 'user', 'property')


class ParcelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Parcel
        fields = ('url', 'id', 'ZIPcode', 'TaxRateArea_CITY', 'AIN', 'RollYear', 'TaxRateArea', 'AssessorID',
                  'PropertyLocation', 'PropertyType', 'PropertyUseCode', 'GeneralUseType', 'SpecificUseType',
                  'SpecificUseDetail1', 'SpecificUseDetail2', 'totBuildingDataLines', 'YearBuilt',
                  'EffectiveYearBuilt', 'SQFTmain', 'Bedrooms', 'Bathrooms', 'Units', 'RecordingDate', 'LandValue',
                  'LandBaseYear', 'ImprovementValue', 'ImpBaseYear', 'TotalLandImpValue', 'HomeownersExemption',
                  'RealEstateExemption', 'FixtureValue', 'FixtureExemption', 'PersonalPropertyValue',
                  'PersonalPropertyExemption', 'isTaxableParcel', 'TotalValue', 'TotalExemption', 'netTaxableValue',
                  'SpecialParcelClassification', 'AdministrativeRegion', 'Cluster', 'ParcelBoundaryDescription',
                  'HouseNo', 'HouseFraction', 'StreetDirection', 'StreetName', 'UnitNo', 'City', 'ZIPcode5', 'rowID',
                  'CENTER_LAT', 'CENTER_LON')
