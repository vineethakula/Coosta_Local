from django.shortcuts import render
from rest_framework import filters
from drf_custom_viewsets.viewsets import CustomSerializerViewSet
from offers.serializers import GetOffersSerializer, PostOffersSerializer
from offers.serializers import GetCounterOffersSerializer
from offers.serializers import PostCounterOffersSerializer
from offers.models import Offers, CounterOffers
from rest_framework.permissions import IsAuthenticated


class OffersViewSet(CustomSerializerViewSet):
    queryset = Offers.objects.all().order_by('-offer_date')
    permission_classes = (IsAuthenticated,)
    serializer_class = GetOffersSerializer

    custom_serializer_classes = {
        'create': PostOffersSerializer,
        'update': PostOffersSerializer
    }
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('id',)
    filter_fields = {
        'property__user': ['exact'],
        'offered_by': ['exact'],
        'property__id': ['exact']
    }


class CounterOffersViewSet(CustomSerializerViewSet):
    queryset = CounterOffers.objects.all()
    permission_classes = (IsAuthenticated,)

    serializer_class = GetCounterOffersSerializer
    custom_serializer_classes = {
        'create': PostCounterOffersSerializer,
        'update': PostCounterOffersSerializer
    }
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    #ordering_fields = ('id',)
    filter_fields = {
        'offer__id': ['exact'],
        'offer__offered_by': ['exact']
    }


def offers(request):
    return render(request, 'offer_management/offers.html')