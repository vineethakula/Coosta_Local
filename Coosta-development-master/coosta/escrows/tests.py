from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.request import Request

from properties.models import Property
from contracts.models import Contract
from rest_framework.test import APIRequestFactory
from .models import *

factory = APIRequestFactory()
request = factory.get('/')
serializer_context = {
    'request': Request(request),
}


class CreateEscrowPropertyTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.user = User.objects.create(username="mike")
        self.user2 = User.objects.create(username="albert")
        self.property = Property.objects.create(property_title='test_Property')
        self.contract = Contract.objects.create(buyer=self.user, seller=self.user2, property=self.property,
                                                last_updated_by=self.user2)

        self.data = {
            'contract': reverse('contract-detail', args=[self.contract.id])
        }

    def test_can_create_escrowproperty(self):
        response = self.client.post(reverse('escrowproperty-list'), self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadEscrowPropertyTest(APITestCase):

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
        self.escrowproperty = EscrowProperty.objects.create(contract=self.contract)

    def test_can_read_escrowproperty_list(self):
        response = self.client.get(reverse('escrowproperty-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_escrowproperty_detail(self):
        response = self.client.get(reverse('escrowproperty-detail', args=[self.escrowproperty.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateEscrowPropertyTest(APITestCase):
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
        self.escrowproperty = EscrowProperty.objects.create(contract=self.contract)

        self.data = {
            'contract': reverse('contract-detail', args=[self.contract.id])
        }

    def test_can_update_escrowproperty(self):
        response = self.client.put(reverse('escrowproperty-detail',
                                           args=[self.escrowproperty.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteEscrowPropertyTest(APITestCase):
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
        self.escrowproperty = EscrowProperty.objects.create(contract=self.contract)

    def test_can_delete_escrowproperty(self):
        response = self.client.delete(reverse('escrowproperty-detail',
                                              args=[self.escrowproperty.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)