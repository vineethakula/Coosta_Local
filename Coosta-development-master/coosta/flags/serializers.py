from rest_framework import serializers

from coosta_users.serializers import UserSerializer
from flags.models import FlaggedProperty, FlagType
from properties.serializers import GetPropertySerializer


class FlagTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FlagType
        fields = '__all__'


class GetFlaggedPropertySerializer(serializers.HyperlinkedModelSerializer):

    property = GetPropertySerializer()
    type_of_flag = FlagTypeSerializer()
    flag_raised_by = UserSerializer()

    class Meta:
        model = FlaggedProperty
        fields = ('id', 'property', 'type_of_flag', 'flag_raised_by',
                  'message', 'flag_raised_datetime')


class PostFlaggedPropertySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FlaggedProperty
        fields = '__all__'
