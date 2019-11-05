from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from properties.models import *
from django.utils import timezone

# Create your models here.


class Coosta_Message(models.Model):
    sender = models.ForeignKey(User, null=True, blank=True, related_name='sender')
    recipient = models.ForeignKey(User, null=True, blank=True, related_name='recipient')
    property = models.ForeignKey(Property, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True,blank=True)
    message_body = models.TextField(null=True,blank=True)
    create_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    read_by_recipient = models.BooleanField(default=False)

    def __repr__(self):
        #TODO
        return "<Message>"

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "Messages"

