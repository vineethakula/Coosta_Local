from rest_framework import serializers
from .models import *
from coosta_users.serializers import UserSerializer


class GetCoostaMessageSerializer(serializers.HyperlinkedModelSerializer):

    sender = UserSerializer(read_only=True)

    class Meta:
        model = Coosta_Message
        fields = ('url', 'id', 'sender', 'recipient', 'property', 'subject', 'message_body',
                  'read_by_recipient', 'create_on')


class PostCoostaMessageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Coosta_Message
        fields = ('url', 'id', 'sender', 'recipient', 'property', 'subject', 'message_body',
                  'read_by_recipient', 'create_on')

