from rest_framework import serializers
from escrows.models import EscrowProperty
from contracts.serializers import GetContractSerializer


class GetEscrowPropertySerializer(serializers.HyperlinkedModelSerializer):
    contract = GetContractSerializer()

    class Meta:
        model = EscrowProperty
        fields = ('id', 'contract', 'deal_closed_by_escrow', 'deal_closed_by_escrow_on', 'escrow_name',
                  'escrow_comments')


class PostEscrowPropertySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = EscrowProperty
        fields = ('id', 'contract', 'deal_closed_by_escrow', 'deal_closed_by_escrow_on', 'escrow_name',
                  'escrow_comments')