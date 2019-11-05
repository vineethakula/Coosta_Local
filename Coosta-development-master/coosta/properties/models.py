from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Images(models.Model):
    """
    This model will keeps the all images of a property.
    """
    image = models.FileField(upload_to='Images/', blank=True, null=True)

    def __repr__(self):
        return "<Images ({0})>".format(self.id)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "Images"


class PropertyImages(models.Model):
    """
    This model will keeps the all images of a property.
    """
    image = models.ForeignKey(Images, blank=True, null=True, related_name='prop_img')
    property = models.ForeignKey('Property', blank=True, null=True, related_name='prop_prop')

    def __repr__(self):
        return "<PropertyImages ({0})>".format(self.property)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "Property Images"


class Property(models.Model):
    user = models.ForeignKey(User, null=True,blank=True)
    search_index = models.CharField(max_length=500, null=True,blank=True)
    property_title = models.CharField(max_length=100, null=True,blank=True)
    address = models.CharField(max_length=100, null=True,blank=True)
    city = models.CharField(max_length=200, null=True,blank=True)
    state = models.CharField(max_length=200, null=True,blank=True)
    zip_code = models.CharField(max_length=15, null=True,blank=True)
    home_type = models.CharField(max_length=200, null=True,blank=True)
    beds = models.IntegerField(default=0, null=True,blank=True)
    property_value = models.IntegerField(default=0, null=True,blank=True)
    baths = models.IntegerField(default=0, null=True,blank=True)
    rooms = models.IntegerField(default=0, null=True,blank=True)
    property_size = models.IntegerField(default=0, null=True,blank=True)
    floors = models.IntegerField(default=0, null=True,blank=True)
    roof = models.BooleanField(default=False)
    basement = models.CharField(max_length=50, null=True,blank=True)
    year_built = models.CharField(max_length=10, null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    other_features = models.TextField(null=True,blank=True)
    status = models.ForeignKey('PropertyStatus', default=1, blank=True, null=True,
                               related_name='property_status')
    images = models.ManyToManyField(Images, blank=True, through=PropertyImages,
                                    related_name='property_images')
    latitude = models.CharField(max_length=50, null=True,blank=True)
    longitude = models.CharField(max_length=50, null=True,blank=True)
    year_renovated = models.CharField(max_length=10, null=True,blank=True)
    car_park = models.CharField(max_length=100, null=True,blank=True)
    listed_on = models.DateField(auto_now_add=True, blank=True, null=True)
    thumbnail = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    def __repr__(self):
        return "<Property ({0})>".format(self.property_title)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "Properties"


class PropertyStatus(models.Model):
    status = models.CharField(max_length=20)

    def __repr__(self):
        return "<Status ({0})>".format(self.status)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "Property status"


class ShortListedProperty(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, related_name='shortlisted_by_user')
    property = models.ForeignKey(Property, null=True, blank=True, related_name='shortlisted_property')
    shortlisted_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __repr__(self):
        return "<Shortlisted Property ({0} {1})>".format(self.user, self.property)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "Shortlisted Properties"


class Parcel(models.Model):
    ZIPcode = models.TextField(null=True,blank=True)
    TaxRateArea_CITY = models.TextField(null=True,blank=True)
    AIN = models.BigIntegerField(null=True,blank=True)
    RollYear = models.IntegerField(null=True,blank=True)
    TaxRateArea = models.TextField(null=True,blank=True)
    AssessorID = models.TextField(null=True,blank=True)
    PropertyLocation = models.TextField(null=True,blank=True)
    PropertyType = models.TextField(null=True,blank=True)
    PropertyUseCode = models.TextField(null=True,blank=True)
    GeneralUseType = models.TextField(null=True,blank=True)
    SpecificUseType = models.TextField(null=True,blank=True)
    SpecificUseDetail1 = models.TextField(null=True,blank=True)
    SpecificUseDetail2 = models.TextField(null=True,blank=True)
    totBuildingDataLines = models.IntegerField(null=True,blank=True)
    YearBuilt = models.IntegerField(null=True,blank=True)
    EffectiveYearBuilt = models.IntegerField(null=True,blank=True)
    SQFTmain = models.IntegerField(null=True,blank=True)
    Bedrooms = models.IntegerField(null=True,blank=True)
    Bathrooms = models.IntegerField(null=True,blank=True)
    Units = models.IntegerField(null=True,blank=True)
    RecordingDate = models.TextField(null=True,blank=True)
    LandValue = models.IntegerField(null=True,blank=True)
    LandBaseYear = models.IntegerField(null=True,blank=True)
    ImprovementValue = models.IntegerField(null=True,blank=True)
    ImpBaseYear = models.IntegerField(null=True,blank=True)
    TotalLandImpValue = models.IntegerField(null=True,blank=True)
    HomeownersExemption = models.IntegerField(null=True,blank=True)
    RealEstateExemption = models.IntegerField(null=True,blank=True)
    FixtureValue = models.IntegerField(null=True,blank=True)
    FixtureExemption = models.IntegerField(null=True,blank=True)
    PersonalPropertyValue = models.IntegerField(null=True,blank=True)
    PersonalPropertyExemption = models.IntegerField(null=True,blank=True)
    isTaxableParcel = models.TextField(null=True,blank=True)
    TotalValue = models.IntegerField(null=True,blank=True)
    TotalExemption = models.IntegerField(null=True,blank=True)
    netTaxableValue = models.IntegerField(null=True,blank=True)
    SpecialParcelClassification = models.TextField(null=True,blank=True)
    AdministrativeRegion = models.TextField(null=True,blank=True)
    Cluster = models.TextField(null=True,blank=True)
    ParcelBoundaryDescription = models.TextField(null=True,blank=True)
    HouseNo = models.IntegerField(null=True,blank=True)
    HouseFraction = models.TextField(null=True,blank=True)
    StreetDirection = models.TextField(null=True,blank=True)
    StreetName = models.TextField(null=True,blank=True)
    UnitNo = models.TextField(null=True,blank=True)
    City = models.TextField(null=True,blank=True)
    ZIPcode5 = models.IntegerField(null=True,blank=True)
    rowID = models.TextField(null=True,blank=True)
    CENTER_LAT = models.DecimalField(max_digits=10, decimal_places=8, null=True,blank=True)
    CENTER_LON = models.DecimalField(max_digits=11, decimal_places=8, null=True,blank=True)

    def __repr__(self):
        return "<Parcel ({0} - {1} - {2})>".format(self.HouseNo, self.StreetName, self.City)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "Parcel"
