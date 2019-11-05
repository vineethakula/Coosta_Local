from rest_framework import serializers
from .models import CoostaNotification, NotificationType
from coosta_users.serializers import UserSerializer
from properties.serializers import GetPropertySerializer


class GetNotificationSerializer(serializers.HyperlinkedModelSerializer):

    shortlisted_by = UserSerializer(read_only=True)
    property_owner = UserSerializer(read_only=True)
    property = GetPropertySerializer(read_only=True)

    class Meta:
        model = CoostaNotification
        fields = ('url', 'id', 'shortlisted_by', 'property_owner', 'property',
                  'title', 'body', 'type', 'read_by_recipient')


class PostNotificationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CoostaNotification
        fields = ('url', 'id', 'shortlisted_by', 'property_owner', 'property',
                  'title', 'body', 'type', 'read_by_recipient')


class NotificationTypeSerializer(serializers.HyperlinkedModelSerializer ):

    class Meta:
        model = NotificationType
        fields = ('url', 'id', 'type')
