from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    profile_image = models.FileField(upload_to='Images/', blank=True,
                                     null=True)
    area_code = models.CharField(max_length=10, blank=True, null=True,
                                 default=None)
    mobile_number = models.CharField(max_length=20, blank=True, null=True,
                                     default=None)
    address = models.CharField(max_length=200, blank=True, null=True,
                               default=None)
    city = models.CharField(max_length=100, blank=True, null=True,
                            default=None)
    town = models.CharField(max_length=100, blank=True, null=True,
                            default=None)
    state = models.CharField(max_length=100, blank=True, null=True,
                             default=None)
    zip_code = models.CharField(max_length=100, blank=True, null=True,
                                default=None)

    def __repr__(self):
        return "<User Profile ({0})>".format(self.user.username)

    def __unicode__(self):
        return self.__repr__()

    def get_profile_image(self):
        if self.profile_image:
            return self.profile_image
        else:
            return "/media/images/unisex_user_logo.png"

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)

    class Meta:
        verbose_name_plural = "User Profiles"


class Documents(models.Model):
    """
    This model will keeps all the users documents.
    """
    file = models.FileField(upload_to='UserDocuments/', blank=True, null=True)

    def __repr__(self):
        return "<User Document ({0})>".format(self.file)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "User Documents"


class PreApprovedDocuments(models.Model):
    pre_approved_user = models.ForeignKey('coosta_users.PreApprovedUser', null=True, blank=True, related_name="pre_approved_user")
    file = models.ForeignKey(Documents, blank=True, null=True, related_name='user_document')

    def __repr__(self):
        return "<Pre-Approved Document ({0})>".format(self.pre_approved_user)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "Pre-Approved Documents"


class NonPreApprovedUser(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,
                             verbose_name="Non Pre-Approved User")
    created_on = models.DateField(auto_now_add=True, blank=True, null=True)

    def __repr__(self):
        return "<Non Pre-Approve User ({0})>".format(self.user.username)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "Non Pre-Approved User"


class PreApprovedUser(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    documents = models.ManyToManyField(Documents, blank=True, through=PreApprovedDocuments,
                                       related_name='pre_approved_documents')
    created_on = models.DateField(auto_now_add=True, blank=True, null=True)

    def __repr__(self):
        return "<Pre-Approve User ({0})>".format(self.user.username)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name_plural = "Pre-Approved User"

