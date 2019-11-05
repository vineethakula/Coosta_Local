from __future__ import unicode_literals

from django.db import models

from properties.models import Property
from django.contrib.auth.models import User


class Offers(models.Model):
    property = models.ForeignKey(Property, null=True, blank=True)
    offered_by = models.ForeignKey(User, null=True, blank=True)
    offer_amount = models.IntegerField(default=0, null=True, blank=True)
    offer_date = models.DateField(auto_now_add=True, blank=True, null=True)

    highest_offer_amount = models.IntegerField(default=0, null=True,
                                               blank=True, editable=False)
    final_accepted_offer = models.ForeignKey("CounterOffers", blank=True,
                                             null=True, default=None)
    accepted = models.BooleanField(default=False)
    #TODO add accepted_on date field

    def save(self, *args, **kwargs):
        # For the first time, highest offer amount will be same as offer amount
        if not self.pk:
            self.highest_offer_amount = self.offer_amount
        super(Offers, self).save(*args, **kwargs)

    def __repr__(self):
        return "<Offer - From {} To {} on Property - {}>".format(
            self.offered_by,
            self.property.user,
            self.property)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "Offers"


class CounterOffers(models.Model):
    offer = models.ForeignKey(Offers, null=True, blank=True)
    counter_offer_amount = models.IntegerField(default=0, null=True,
                                               blank=True)
    counter_offer_date = models.DateField(auto_now_add=True, blank=True,
                                          null=True)
    offered_by = models.ForeignKey(User, null=True, blank=True)

    #counter_offer_accepted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # For subsequent entries in CounterOffers table, Whatever will be the
        # highest counter offer, will set highest amount in Offers table
        if self.counter_offer_amount > self.offer.highest_offer_amount and self.offered_by != self.offer.property.user:
            self.offer.highest_offer_amount = self.counter_offer_amount
            self.offer.save()
        super(CounterOffers, self).save(*args, **kwargs)

    def __repr__(self):
        return "<CounterOffer, On Offer - {}, amount - {}>".format(
            self.offer,
            self.counter_offer_amount)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "Counter Offers"
