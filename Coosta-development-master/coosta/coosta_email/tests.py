from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.request import Request

from .serializers import SendEmailSerializer, PasswordResetSerializer,\
    PasswordResetConfirmSerializer
from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()
request = factory.get('/')
serializer_context = {
    'request': Request(request),
}


class CreateSendEmailViewTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'winteriscoming')
        self.client.login(username='john', password='winteriscoming')

    def test_can_send_email_view(self):
        response = self.client.post(reverse('send_email'),
                                    {
                                        'subject': 'Test mail from coosta',
                                        'message': 'This is test email',
                                        'from_email': 'sheilasmith.coosta@gmail.com',
                                        'recipient_list': [
                                            'deepak.k.tewatia@gmail.com',]
                                    })
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PasswordResetSerializerTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'winteriscoming')
        self.client.login(username='john', password='winteriscoming')

    def test_can_reset_password(self):
        response = self.client.post(reverse('password_reset'),
                                    {'bla':'bla'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
