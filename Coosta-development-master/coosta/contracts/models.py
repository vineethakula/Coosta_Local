from __future__ import unicode_literals

from django.db import models
from properties.models import Property
from escrows.models import EscrowProperty
from offers.models import Offers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Contract(models.Model):
    offer = models.ForeignKey(Offers, null=True, blank=True)
    property = models.ForeignKey(Property, null=True, blank=True)
    buyer = models.ForeignKey(User, null=True, blank=True, related_name='buyer')
    seller = models.ForeignKey(User, null=True, blank=True, related_name='seller')
    signed_by_seller = models.BooleanField(default=False)
    signed_by_buyer = models.BooleanField(default=False)
    signed_by_seller_on = models.DateTimeField(blank=True, null=True)
    signed_by_buyer_on = models.DateTimeField(blank=True, null=True)
    signed_by_seller_at = models.CharField(max_length=200, blank=True, null=True)
    signed_by_buyer_at = models.CharField(max_length=200, blank=True, null=True)
    last_updated_on = models.DateTimeField(auto_now_add=True)
    last_updated_by = models.ForeignKey(User, blank=True, null=True, default=None, related_name='last_updated_by')

    def __repr__(self):
        return "<Contract Signed for Property ({0})>".format(self.property)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "Contracts"

    def save(self, *args, **kwargs):
        # Applying restriction so that only one contract object is created for one Offer
        if not self.pk and Contract.objects.filter(offer=self.offer):
            raise ValidationError('One Contract object already exist for given offer')
        else:
            if self.signed_by_seller and self.signed_by_buyer:
                escrow_property = EscrowProperty.objects.filter(contract__id=self.id)
                if not escrow_property:
                    escrow_property = EscrowProperty()
                    escrow_property.contract = self
                    escrow_property.save()
            super(Contract, self).save(*args, **kwargs)
