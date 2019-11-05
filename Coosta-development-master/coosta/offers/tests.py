from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.request import Request

from properties.models import Property
from offers.models import Offers, CounterOffers
from rest_framework.test import APIRequestFactory


factory = APIRequestFactory()
request = factory.get('/')
serializer_context = {
    'request': Request(request),
}


class CreateOffersTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.test_user = User.objects.create(username="bob")
        self.test_user2 = User.objects.create(username="thebuilder")
        self.property = Property.objects.create(property_title='test_Property')
        self.offer_amount = 1000

        self.data = {
            'property': reverse('property-detail', args=[self.property.id]),
            'offered_by': reverse('user-detail', args=[self.test_user.id]),
            'offer_amount': self.offer_amount,
        }

    def test_can_create_offer(self):
        response = self.client.post(reverse('offers-list'), self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadOffersTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.test_user = User.objects.create(username="bob")
        self.test_user2 = User.objects.create(username="thebuilder")
        self.property = Property.objects.create(property_title='test_Property')
        self.offer_amount = 1000

        self.offer = Offers.objects.create(property=self.property,
                                           offered_by=self.test_user,
                                           offer_amount=self.offer_amount)

    def test_can_read_offers_list(self):
        response = self.client.get(reverse('offers-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_offers_detail(self):
        response = self.client.get(reverse('offers-detail',
                                           args=[self.offer.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateOffersTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.test_user = User.objects.create(username="bob")
        self.test_user2 = User.objects.create(username="thebuilder")
        self.property = Property.objects.create(property_title='test_Property')
        self.property2 = Property.objects.create(property_title='test_prop2')
        self.offer_amount = 1000
        self.offer_amount2 = 21000

        self.offer = Offers.objects.create(property=self.property,
                                           offered_by=self.test_user,
                                           offer_amount=self.offer_amount)

        self.data = {
            'property': reverse('property-detail', args=[self.property.id]),
            'offered_by': reverse('user-detail', args=[self.test_user2.id]),
            'offer_amount': self.offer_amount2,
        }

    def test_can_update_offers(self):
        response = self.client.put(reverse('offers-detail',
                                           args=[self.offer.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteOffersTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.test_user = User.objects.create(username="bob")
        self.test_user2 = User.objects.create(username="thebuilder")
        self.property = Property.objects.create(property_title='test_Property')
        self.offer_amount = 1000

        self.offer = Offers.objects.create(property=self.property,
                                           offered_by=self.test_user,
                                           offer_amount=self.offer_amount)

    def test_can_delete_offer(self):
        response = self.client.delete(reverse('offers-detail',
                                              args=[self.offer.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateCounterOffersTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.test_user = User.objects.create(username="bob")
        self.property = Property.objects.create(property_title='test_Property')
        self.offer_amount = 1000

        self.counter_offer_amount = 2000

        self.offer = Offers.objects.create(property=self.property,
                                           offered_by=self.test_user,
                                           offer_amount=self.offer_amount)

        self.data = {
            'offer': reverse('offers-detail', args=[self.offer.id]),
            'counter_offer_amount': self.counter_offer_amount,
            'offered_by': reverse('user-detail', args=[self.test_user.id]),
        }

    def test_can_create_Counteroffer(self):
        response = self.client.post(reverse('counteroffers-list'), self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadCounterOffersTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.test_user = User.objects.create(username="bob")
        self.property = Property.objects.create(property_title='test_Property')
        self.offer_amount = 1000

        self.counter_offer_amount = 2000

        self.offer = Offers.objects.create(property=self.property,
                                           offered_by=self.test_user,
                                           offer_amount=self.offer_amount)

        self.counter_offer = CounterOffers.objects.create(
            offer=self.offer,
            counter_offer_amount=self.counter_offer_amount,
            offered_by=self.test_user,
        )

    def test_can_read_counter_offers_list(self):
        response = self.client.get(reverse('counteroffers-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_counter_offers_detail(self):
        response = self.client.get(reverse('counteroffers-detail',
                                           args=[self.offer.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateCounterOffersTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.test_user = User.objects.create(username="bob")
        self.property = Property.objects.create(property_title='test_Property')
        self.offer_amount = 1000

        self.counter_offer_amount = 2000

        self.offer = Offers.objects.create(property=self.property,
                                           offered_by=self.test_user,
                                           offer_amount=self.offer_amount)

        self.counter_offer = CounterOffers.objects.create(
            offer=self.offer,
            counter_offer_amount=self.counter_offer_amount,
            offered_by=self.test_user,
        )

        self.data = {
            'offer': reverse('offers-detail', args=[self.offer.id]),
            'counter_offer_amount': self.counter_offer_amount,
            'offered_by': reverse('user-detail', args=[self.test_user.id]),
        }

    def test_can_update_counter_offers(self):
        response = self.client.put(reverse('counteroffers-detail',
                                           args=[self.counter_offer.id]),
                                   self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteCounterOffersTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.test_user = User.objects.create(username="bob")
        self.test_user2 = User.objects.create(username="thebuilder")
        self.property = Property.objects.create(property_title='test_Property')
        self.offer_amount = 1000

        self.counter_offer_amount = 2000

        self.offer = Offers.objects.create(property=self.property,
                                           offered_by=self.test_user,
                                           offer_amount=self.offer_amount)

        self.counter_offer = CounterOffers.objects.create(
            offer=self.offer,
            counter_offer_amount=self.counter_offer_amount,
            offered_by=self.test_user,
        )

    def test_can_delete_counter_offer(self):
        response = self.client.delete(reverse('counteroffers-detail',
                                              args=[self.counter_offer.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
