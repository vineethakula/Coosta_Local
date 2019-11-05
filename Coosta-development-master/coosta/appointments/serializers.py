from rest_framework import serializers
from coosta_users.serializers import UserSerializer
from properties.serializers import GetPropertySerializer
from appointments.models import OpenHouse, OpenHouseRSVP, OwnerAvailability, AppointmentRequest


class PostOpenHouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenHouse
        fields = ('id', 'property', 'date', 'start_time', 'end_time')


class GetOpenHouseSerializer(PostOpenHouseSerializer):
    property = GetPropertySerializer()

    PostOpenHouseSerializer.Meta.fields = '__all__'


class PostOpenHouseRSVPSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenHouseRSVP
        fields = ('id', 'open_house', 'rsvp_user')


class GetOpenHouseRSVPSerializer(PostOpenHouseRSVPSerializer):
    open_house = GetOpenHouseSerializer()
    rsvp_user = UserSerializer()

    PostOpenHouseRSVPSerializer.Meta.fields = '__all__'


class GetOwnerAvailabilitySerializer(serializers.HyperlinkedModelSerializer):

    property = GetPropertySerializer()

    class Meta:
        model = OwnerAvailability
        fields = ('id', 'property', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
                  'wkd_start_time', 'wkd_end_time', 'wknd_start_time', 'wknd_end_time', 'created_on')


class PostOwnerAvailabilitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OwnerAvailability
        fields = ('id', 'property', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
                  'wkd_start_time', 'wkd_end_time', 'wknd_start_time', 'wknd_end_time')


class GetAppointmentRequestSerializer(serializers.HyperlinkedModelSerializer):

    owner_availability = GetOwnerAvailabilitySerializer()
    buyer = UserSerializer()

    class Meta:
        model = AppointmentRequest
        fields = ('id', 'owner_availability', 'buyer', 'requested_time', 'requested_date', 'requested_on',
                  'approved_by_seller', 'approved_on', 'rejected_by_seller', 'rejected_on', 'cancelled_by_buyer',
                  'cancelled_on')


class PostAppointmentRequestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AppointmentRequest
        fields = ('id', 'owner_availability', 'buyer', 'requested_time', 'requested_date', 'approved_by_seller',
                  'approved_on', 'rejected_by_seller', 'rejected_on', 'cancelled_by_buyer', 'cancelled_on')