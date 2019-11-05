from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_custom_viewsets.viewsets import CustomSerializerViewSet


class NotificationViewSet(CustomSerializerViewSet):
    """
    API endpoint for Notifications
    """
    permission_classes = (IsAuthenticated,)
    queryset = CoostaNotification.objects.all()
    serializer_class = GetNotificationSerializer
    custom_serializer_classes = {
        'create': PostNotificationSerializer,
        'update': PostNotificationSerializer,
    }
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('create_on')
    filter_fields = {
            'id': ['lte', 'gte'],
            'create_on': ['lte', 'gte'],
            'property_owner': ['exact'],
        }


class NotificationTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Notification Types
    """
    permission_classes = (IsAuthenticated,)
    queryset = NotificationType.objects.all()
    serializer_class = NotificationTypeSerializer

