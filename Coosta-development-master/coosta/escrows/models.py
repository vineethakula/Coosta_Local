from __future__ import unicode_literals

from django.db import models


class EscrowProperty(models.Model):
    contract = models.ForeignKey('contracts.Contract', null=True, blank=True)
    deal_closed_by_escrow = models.BooleanField(default=False)
    deal_closed_by_escrow_on = models.DateTimeField(blank=True, null=True)
    escrow_name = models.CharField(max_length=100, blank=True, null=True)
    escrow_comments = models.CharField(max_length=500, blank=True, null=True)

    def __repr__(self):
        return "<Escrow For Property ({0})>".format(self.contract.property.property_title)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "Escrow Properties"


