from django.db.models import Q
from rest_framework import filters
from django.shortcuts import render
from escrows.models import EscrowProperty
from rest_framework.permissions import IsAuthenticated
from drf_custom_viewsets.viewsets import CustomSerializerViewSet
from escrows.serializers import GetEscrowPropertySerializer, PostEscrowPropertySerializer


class EscrowPropertyViewSet(CustomSerializerViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = EscrowProperty.objects.all()
    serializer_class = GetEscrowPropertySerializer
    custom_serializer_classes = {
        'create': PostEscrowPropertySerializer,
        'update': PostEscrowPropertySerializer,
    }
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = {
        'contract__id': ['exact']
    }


def closing_agent(request, closing_agent_id):
    try:
        closing_agent = EscrowProperty.objects.get(Q(id=closing_agent_id), Q(contract__buyer=request.user) | Q(contract__seller=request.user))
        return render(request, 'escrow//closing_agent.html')
    except:
        raise Exception(403, "Permission Denied")