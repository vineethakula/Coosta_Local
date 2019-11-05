from __future__ import unicode_literals

from django.db import models

from coosta_users.models import User
from properties.models import Property


class FlagType(models.Model):
    """
    Types of Flags that can be raised 
    """

    # Unique true makes sure that flag names are not repeated
    flag_type_name = models.CharField(unique=True, max_length=20)

    def __repr__(self):
        return "<Flag Type ({0})>".format(self.flag_type_name)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "Flag Types"


class FlaggedProperty(models.Model):
    """
    Flagged properties
    """
    property = models.ForeignKey(Property, null=True, blank=True)
    type_of_flag = models.ForeignKey(FlagType, null=True, blank=True)
    flag_raised_datetime = models.DateTimeField(auto_now_add=True, null=True,
                                                blank=True)
    flag_raised_by = models.ForeignKey(User, null=True, blank=True)
    message = models.CharField(max_length=200, null=True, blank=True)

    def __repr__(self):
        return "<Flagged Property : {} by {}".format(self.property,
                                                     self.flag_raised_by)

    def __unicode__(self):
        return self.__repr__()

    def save(self, *args, **kwargs):
        # To make sure that a user should not be able to flag the same property
        # with same Flag type more than once.
        #
        # Example: Jon snow wont be able to flag The Wall(property) with
        # `Wrong Description`(Flag Type) many times.
        if FlaggedProperty.objects.filter(property=self.property,
                                          type_of_flag=self.type_of_flag
                                          ).count():
            raise ValueError('Cannot report same property with same issue '
                             'multiple times')
        super(FlaggedProperty, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Flagged Properties"
