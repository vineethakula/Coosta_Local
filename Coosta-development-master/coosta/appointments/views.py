from rest_framework import filters
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from drf_custom_viewsets.viewsets import CustomSerializerViewSet
from appointments.models import OpenHouse, OpenHouseRSVP, OwnerAvailability, AppointmentRequest
#removed multiple import of from appointments.serializers in signle import
from appointments.serializers import GetOpenHouseSerializer, PostOpenHouseSerializer, GetOpenHouseRSVPSerializer, \
    PostOpenHouseRSVPSerializer, GetOwnerAvailabilitySerializer, PostOwnerAvailabilitySerializer, \
    GetAppointmentRequestSerializer, PostAppointmentRequestSerializer


class OpenHouseViewSet(CustomSerializerViewSet):
    queryset = OpenHouse.objects.all().order_by('created_on')
    permission_classes = (IsAuthenticated,)

    serializer_class = GetOpenHouseSerializer

    custom_serializer_classes = dict.fromkeys(['create', 'update'],
                                              PostOpenHouseSerializer)

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('id',)
    filter_fields = {
        'property__user': ['exact']
    }


class OpenHouseRSVPViewSet(CustomSerializerViewSet):
    queryset = OpenHouseRSVP.objects.all().order_by('created_on')
    permission_classes = (IsAuthenticated,)

    serializer_class = GetOpenHouseRSVPSerializer

    custom_serializer_classes = dict.fromkeys(['create', 'update'],
                                              PostOpenHouseRSVPSerializer)

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('id',)
    filter_fields = {
        'open_house': ['exact'],
        'rsvp_user': ['exact'],
        'open_house__property__user': ['exact'],
    }


def openhousersvp_for_seller(request):
    return render(request, 'appointments/openhousersvp_for_seller.html')


class OwnerAvailabilityViewSet(CustomSerializerViewSet):
    queryset = OwnerAvailability.objects.all().order_by('created_on')
    permission_classes = (IsAuthenticated,)

    serializer_class = GetOwnerAvailabilitySerializer

    custom_serializer_classes = dict.fromkeys(['create', 'update'],
                                              PostOwnerAvailabilitySerializer)


class AppointmentRequestViewSet(CustomSerializerViewSet):
    queryset = AppointmentRequest.objects.all()
    permission_classes = (IsAuthenticated,)

    serializer_class = GetAppointmentRequestSerializer

    custom_serializer_classes = dict.fromkeys(['create', 'update'],
                                              PostAppointmentRequestSerializer)