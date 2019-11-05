from __future__ import unicode_literals

from django.db import models
from properties.models import Property
from django.contrib.auth.models import User


class PageView(models.Model):
    property = models.ForeignKey(Property, null=True, blank=True)
    viewed_by = models.ForeignKey(User, null=True, blank=True)
    viewed_on = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return "<PageView ({0}), viewed by ({1})>".format(self.property,
                                                          self.viewed_by)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "Page Views"
