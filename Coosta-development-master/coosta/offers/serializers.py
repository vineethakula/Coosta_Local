from rest_framework import serializers
from offers.models import Offers, CounterOffers
from properties.serializers import GetPropertySerializer
from coosta_users.serializers import UserSerializer


class GetOffersSerializer(serializers.HyperlinkedModelSerializer):
    property = GetPropertySerializer()
    offered_by = UserSerializer()

    class Meta:
        model = Offers
        fields = ('id', 'property', 'offered_by', 'offer_amount', 'offer_date',
                  'highest_offer_amount', 'final_accepted_offer', 'accepted')


class PostOffersSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Offers
        fields = ('id', 'property', 'offered_by', 'offer_amount', 'offer_date',
                  'highest_offer_amount', 'final_accepted_offer', 'accepted')


class GetCounterOffersSerializer(serializers.HyperlinkedModelSerializer):
    offer = GetOffersSerializer()
    offered_by = UserSerializer()

    class Meta:
        model = CounterOffers
        fields = ('id', 'offer', 'counter_offer_amount', 'counter_offer_date',
                  'offered_by')


class PostCounterOffersSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CounterOffers
        fields = ('id', 'offer', 'counter_offer_amount', 'counter_offer_date',
                  'offered_by')
