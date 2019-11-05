from django.db.models import Q
from rest_framework import filters
from django.shortcuts import render
from contracts.models import Contract
from rest_framework.permissions import IsAuthenticated
from drf_custom_viewsets.viewsets import CustomSerializerViewSet
from contracts.serializers import GetContractSerializer, PostContractSerializer


class ContractViewSet(CustomSerializerViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Contract.objects.all().order_by('-last_updated_by')
    serializer_class = GetContractSerializer
    custom_serializer_classes = {
        'create': PostContractSerializer,
        'update': PostContractSerializer,
    }
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = {
        'property__id': ['exact'],
        'offer__id': ['exact']
    }


def sign_contract(request, contract_id):
    try:
        contract = Contract.objects.get(Q(id=contract_id), Q(buyer=request.user) | Q(seller=request.user))
        return render(request, 'contract/contract.html', {'contract_id': contract.id})
    except:
        raise Exception(403, "Permission Denied")