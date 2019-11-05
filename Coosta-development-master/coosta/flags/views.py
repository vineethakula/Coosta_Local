from drf_custom_viewsets.viewsets import CustomSerializerViewSet
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from flags.models import FlagType, FlaggedProperty
from flags.serializers import FlagTypeSerializer, \
    GetFlaggedPropertySerializer, \
    PostFlaggedPropertySerializer


class FlagTypeViewSet(viewsets.ModelViewSet):
    queryset = FlagType.objects.all()
    serializer_class = FlagTypeSerializer
    permission_classes = (IsAuthenticated,)


class FlaggedPropertyViewSet(CustomSerializerViewSet):
    queryset = FlaggedProperty.objects.all()

    permission_classes = (IsAuthenticated,)

    serializer_class = GetFlaggedPropertySerializer

    custom_serializer_classes = dict.fromkeys(
        ['create', 'update'],
        PostFlaggedPropertySerializer
    )
