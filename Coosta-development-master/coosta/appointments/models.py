from __future__ import unicode_literals

from django.db import models
from properties.models import Property
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class OpenHouse(models.Model):
    """
        Contains all schedule for open house for all the Property.
    """
    property = models.ForeignKey(Property, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __repr__(self):
        return "<OpenHouse Created for Property ({0})>".format(self.property)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "OpenHouses"


class OpenHouseRSVP(models.Model):
    """
        Contains all attendees information who click on rsvp button on 
        particular property open-house..
    """
    open_house = models.ForeignKey(OpenHouse, null=True, blank=True)
    rsvp_user = models.ForeignKey(User, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        # For subsequent entries in CounterOffers table, Whatever will be the
        # highest counter offer, will set highest amount in Offers table
        if not self.pk and OpenHouseRSVP.objects.filter(open_house=self.open_house, rsvp_user=self.rsvp_user):
            raise ValidationError('You are already marked for this Open House')
        super(OpenHouseRSVP, self).save(*args, **kwargs)

    def __repr__(self):
        return "<User ({0} Selected RSVP for OpenHouse on {1})>".format(
            self.rsvp_user, self.open_house.property
        )

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "OpenHouseRSVPs"


class OwnerAvailability(models.Model):
    """
        contains owner availability for properties
    """
    property = models.ForeignKey(Property, null=True, blank=True)
    sunday = models.BooleanField(default=False)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    wkd_start_time = models.TimeField(null=True, blank=True)
    wkd_end_time = models.TimeField(null=True, blank=True)
    wknd_start_time = models.TimeField(null=True, blank=True)
    wknd_end_time = models.TimeField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk and OwnerAvailability.objects.filter(property=self.property):
            raise ValidationError('You have already set your availability for this property')
        super(OwnerAvailability, self).save(*args, **kwargs)

    def __repr__(self):
        return "<({0} Owner - {1}, Set his/her Availability)>".format(
            self.property.property_title, self.property.user
        )

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "OwnerAvailabilities"


class AppointmentRequest(models.Model):
    """
        Contains all the appointment requests from buyer
    """
    owner_availability = models.ForeignKey(OwnerAvailability, null=True, blank=True)
    buyer = models.ForeignKey(User, null=True, blank=True)
    requested_time = models.TimeField(null=True, blank=True)
    requested_date = models.DateField(null=True, blank=True)
    requested_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    approved_by_seller = models.BooleanField(default=False)
    approved_on = models.DateField(blank=True, null=True)
    rejected_by_seller = models.BooleanField(default=False)
    rejected_on = models.DateField(blank=True, null=True)
    cancelled_by_buyer = models.BooleanField(default=False)
    cancelled_on = models.DateField(blank=True, null=True)

    def __repr__(self):
        return "<Buyer ({0}, made an appointment request for property - {1})>".format(
            self.buyer, self.owner_availability.property.property_title
        )

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "Appointment Requests"