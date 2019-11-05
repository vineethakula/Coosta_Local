from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from properties.models import Property


class NotificationType(models.Model):
    type = models.TextField(null=True, blank=True)

    def __repr__(self):
        return "<Notification Type ({0})>".format(self.type)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "Notification Types"


class CoostaNotification(models.Model):
    shortlisted_by = models.ForeignKey(User, null=True, blank=True, related_name='shortlisted_by')
    property_owner = models.ForeignKey(User, null=True, blank=True, related_name='property_owner')
    property = models.ForeignKey(Property, null=True, blank=True)
    title = models.TextField(null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    type = models.ForeignKey(NotificationType, null=True, blank=True)
    create_on = models.DateTimeField(max_length=10, auto_created=True, null=True, blank=True)
    read_by_recipient = models.BooleanField(default=False)

    def __repr__(self):
        return "<Notification ({0} to {1})>".format(self.title, self.body)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "Notifications"

