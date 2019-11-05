from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.request import Request

from properties.models import Property
from rest_framework.test import APIRequestFactory
from .models import *

factory = APIRequestFactory()
request = factory.get('/')
serializer_context = {
    'request': Request(request),
}


class CreateContractTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.user = User.objects.create(username="mike")
        self.user2 = User.objects.create(username="albert")
        self.property = Property.objects.create(property_title='test_Property')

        self.data = {
            'buyer': reverse('user-detail', args=[self.user.id]),
            'seller': reverse('user-detail', args=[self.user2.id]),
            'property': reverse('property-detail', args=[self.property.id]),
            'last_updated_by': reverse('user-detail', args=[self.user2.id])
        }

    def test_can_create_contract(self):
        response = self.client.post(reverse('contract-list'), self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadContractTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.user = User.objects.create(username="mike")
        self.user2 = User.objects.create(username="albert")
        self.property = Property.objects.create(property_title='test_Property')
        self.contract = Contract.objects.create(seller=self.user2, buyer=self.user, property=self.property,
                                                last_updated_by=self.user2)

    def test_can_read_contract_list(self):
        response = self.client.get(reverse('contract-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_contract_detail(self):
        response = self.client.get(reverse('contract-detail', args=[self.contract.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateContractTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.user = User.objects.create(username="mike")
        self.user2 = User.objects.create(username="albert")
        self.property = Property.objects.create(property_title='test_Property')
        self.contract = Contract.objects.create(seller=self.user2, buyer=self.user, property=self.property,
                                                last_updated_by=self.user2)

        self.data = {
            'buyer': reverse('user-detail', args=[self.user.id]),
            'seller': reverse('user-detail', args=[self.user2.id]),
            'property': reverse('property-detail', args=[self.property.id]),
            'last_updated_by': reverse('user-detail', args=[self.user2.id])
        }

    def test_can_update_contract(self):
        response = self.client.put(reverse('contract-detail',
                                           args=[self.contract.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteContractTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.user = User.objects.create(username="mike")
        self.user2 = User.objects.create(username="albert")
        self.property = Property.objects.create(property_title='test_Property')
        self.contract = Contract.objects.create(seller=self.user2, buyer=self.user, property=self.property,
                                                last_updated_by=self.user2)

    def test_can_delete_contract(self):
        response = self.client.delete(reverse('contract-detail',
                                              args=[self.contract.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)