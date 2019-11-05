from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.request import Request

from properties.models import Property
from models import PageView
from rest_framework.test import APIRequestFactory
from .models import *

factory = APIRequestFactory()
request = factory.get('/')
serializer_context = {
    'request': Request(request),
}


class CreatePageViewTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.user = User.objects.create(username="mike")
        self.property = Property.objects.create(property_title='test_Property')

        self.data = {
            'viewed_by': reverse('user-detail', args=[self.user.id]),
            'property': reverse('property-detail', args=[self.property.id])
        }

    def test_can_create_page_view(self):
        response = self.client.post(reverse('pageview-list'), self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadPageViewTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.user = User.objects.create(username="mike")
        self.property = Property.objects.create(property_title='test_Property')
        self.page_view = PageView.objects.create(viewed_by=self.user, property=self.property)

    def test_can_read_page_view_list(self):
        response = self.client.get(reverse('pageview-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_page_view_detail(self):
        response = self.client.get(reverse('pageview-detail', args=[self.page_view.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdatePageViewTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.user = User.objects.create(username="mike")
        self.property1 = Property.objects.create(property_title='test_Property1')
        self.property2 = Property.objects.create(property_title='test_Property2')
        self.page_view = PageView.objects.create(viewed_by=self.user, property=self.property1)

        self.data = {
            'viewed_by': reverse('user-detail', args=[self.user.id]),
            'property': reverse('property-detail', args=[self.property2.id])
        }

    def test_can_update_page_view(self):
        response = self.client.put(reverse('pageview-detail',
                                           args=[self.property1.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeletePageViewTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.user = User.objects.create(username="mike")
        self.property = Property.objects.create(property_title='test_Property')
        self.page_view = PageView.objects.create(viewed_by=self.user, property=self.property)

    def test_can_delete_page_view(self):
        response = self.client.delete(reverse('pageview-detail',
                                              args=[self.property.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
