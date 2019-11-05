from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.request import Request

from coosta_messages.serializers import *
from rest_framework.test import APIRequestFactory
from .models import *
from properties.models import *

factory = APIRequestFactory()
request = factory.get('/')
serializer_context = {
    'request': Request(request),
}


class CreateMessageTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.property = Property.objects.create(user=self.user, property_title='New Homes in Las Vegas NV')
        self.data = {'sender': reverse('user-detail', args=[self.superuser.id]),
                     'recipient': reverse('user-detail', args=[self.user.id]),
                     'property': reverse('property-detail', args=[self.property.id]), 'subject': 'Test',
                     'message_body': "Your Property Looks Good. I am intrested."}

    def test_can_create_message(self):
        response = self.client.post(reverse('coosta_message-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadMessageTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.property = Property.objects.create(user=self.user, property_title='New Homes in Las Vegas NV')
        self.message = Coosta_Message.objects.create(sender=self.superuser, recipient=self.user, property=self.property,
                                                     subject="Test",
                                                     message_body="Your Property Looks Good. I am intrested.")

    def test_can_read_message_list(self):
        response = self.client.get(reverse('coosta_message-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_messgae_detail(self):
        response = self.client.get(reverse('coosta_message-detail', args=[self.message.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateMessageTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.property = Property.objects.create(user=self.user, property_title='New Homes in Las Vegas NV')
        self.message = Coosta_Message.objects.create(sender=self.superuser, recipient=self.user, property=self.property,
                                                     subject="Test",
                                                     message_body="Your Property Looks Good. I am intrested.")
        self.data = PostCoostaMessageSerializer(self.message, context=serializer_context).data
        self.data.update({'message_body': "Test Update"})
        self.data.pop('sender')
        self.data.pop('recipient')
        self.data.pop('property')

    def test_can_update_property(self):
        response = self.client.put(reverse('coosta_message-detail', args=[self.message.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteMessageTest(APITestCase):
    def setUp(self):

        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.property = Property.objects.create(user=self.user, property_title='New Homes in Las Vegas NV')
        self.message = Coosta_Message.objects.create(sender=self.superuser, recipient=self.user, property=self.property,
                                                     subject="Test",
                                                     message_body="Your Property Looks Good. I am intrested.")

    def test_can_delete_message(self):
        response = self.client.delete(reverse('coosta_message-detail', args=[self.message.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
