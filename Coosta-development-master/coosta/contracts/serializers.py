from contracts.models import Contract
from rest_framework import serializers
from coosta_users.serializers import UserSerializer
from properties.serializers import GetPropertySerializer
from offers.serializers import GetOffersSerializer


class GetContractSerializer(serializers.HyperlinkedModelSerializer):

    buyer = UserSerializer()
    seller = UserSerializer()
    last_updated_by = UserSerializer()
    property = GetPropertySerializer()
    offer = GetOffersSerializer()

    class Meta:
        model = Contract
        fields = ('id', 'offer', 'property', 'buyer', 'seller', 'signed_by_seller', 'signed_by_buyer', 'signed_by_seller_on',
                  'signed_by_buyer_on', 'signed_by_seller_at', 'signed_by_buyer_at', 'last_updated_on',
                  'last_updated_by')


class PostContractSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Contract
        fields = ('id', 'offer', 'property', 'buyer', 'seller', 'signed_by_seller', 'signed_by_buyer', 'signed_by_seller_on',
                  'signed_by_buyer_on', 'signed_by_seller_at', 'signed_by_buyer_at', 'last_updated_by')