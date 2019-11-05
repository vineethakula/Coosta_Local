from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.request import Request

from .serializers import PostNotificationSerializer, NotificationTypeSerializer
from rest_framework.test import APIRequestFactory
from .models import CoostaNotification, NotificationType

factory = APIRequestFactory()
request = factory.get('/')
serializer_context = {
    'request': Request(request),
}


class CreateNotificationViewSetTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'winteriscoming')
        self.client.login(username='john', password='winteriscoming')

    def test_can_create_notification_type(self):
        response = self.client.post(reverse('notificationtype-list'),
                                    {'type': 'type123'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadNotificationViewSetTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john',
                                                       'john@snow.com',
                                                       'winteriscoming')
        self.client.login(username='john', password='winteriscoming')
        self.notification = NotificationType.objects.create(type='type123')

    def test_can_get_notification_type(self):
        response = self.client.get(reverse('notificationtype-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['type'], 'type123')


class UpdateNotificationViewSetTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john',
                                                       'john@snow.com',
                                                       'winteriscoming')
        self.client.login(username='john', password='winteriscoming')
        self.notification = NotificationType.objects.create(type='type123')
        self.data = NotificationTypeSerializer(self.notification, context=serializer_context).data
        self.data.update({'type': 'i am a changed type now'})

    def test_can_update_notification_type(self):
        response = self.client.put(reverse('notificationtype-detail',
                                           args=[self.notification.id])
                                   , self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['type'],  'i am a changed type now')


class DeleteNotificationViewSetTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john',
                                                       'john@snow.com',
                                                       'winteriscoming')
        self.client.login(username='john', password='winteriscoming')
        self.notification = NotificationType.objects.create(type='type123')

    def test_can_delete_notification_type(self):
        response = self.client.delete(reverse('notificationtype-detail',
                                           args=[self.notification.id]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
