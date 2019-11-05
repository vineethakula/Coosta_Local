from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request
from django.core.urlresolvers import reverse
from rest_framework import status

from flags.models import FlagType, FlaggedProperty
from django.utils import timezone
from properties.models import Property

factory = APIRequestFactory()
request = factory.get('/')
serializer_context = {
    'request': Request(request),
}


class CreateFlagTypeTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.data = {'flag_type_name': 'test_flag'}

    def test_can_create_flagtype(self):
        response = self.client.post(reverse('flagtype-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadFlagTypeTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.flag_type = FlagType.objects.create(flag_type_name='test_flag1')

    def test_can_read_flagtype(self):
        response = self.client.get(reverse('flagtype-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_flagtype_detail(self):
        response = self.client.get(reverse('flagtype-detail',
                                           args=[self.flag_type.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateFlagTypeTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.flag_type = FlagType.objects.create(flag_type_name='test_flag1')

        self.data = {
            'flag_type_name': 'new_type',
        }

    def test_can_update_flagtype(self):
        response = self.client.put(reverse('flagtype-detail',
                                           args=[self.flag_type.id]),
                                   self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteFlagTypeTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.flag_type = FlagType.objects.create(
            flag_type_name='test_flag_type'
        )

    def test_can_delete_flagtype(self):
        response = self.client.delete(reverse('flagtype-detail',
                                              args=[self.flag_type.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateFlaggedPropertyTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.property = Property.objects.create(property_title='test_Property')
        self.type_of_flag = FlagType.objects.create(flag_type_name='test_flag')
        self.flag_raised_by = User.objects.create(username="bob")
        self.message = 'This property is mine'

        self.data = {
            'property': reverse('property-detail',
                                  args=[self.property.id]),
            'type_of_flag': reverse('flagtype-detail',
                                    args=[self.type_of_flag.id]),
            'flag_raised_by':reverse('user-detail',
                                    args=[self.flag_raised_by.id]),
            'message': ' test_message',
        }

    def test_can_create_flagged_property(self):
        response = self.client.post(reverse('flaggedproperty-list'), self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadFlaggedPropertyTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.property = Property.objects.create(property_title='test_Property')
        self.type_of_flag = FlagType.objects.create(flag_type_name='test_flag')
        self.flag_raised_by = User.objects.create(username="bob")
        self.message = 'This property is mine'

        self.flagged_property = FlaggedProperty.objects.create(
            property=self.property,
            type_of_flag=self.type_of_flag,
            flag_raised_by=self.flag_raised_by,
            message=self.message
        )

    def test_can_read_flagged_property_list(self):
        response = self.client.get(reverse('flaggedproperty-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_flagged_property_detail(self):
        response = self.client.get(reverse('flaggedproperty-detail',
                                           args=[self.flagged_property.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateFlaggedPropertyTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.property = Property.objects.create(property_title='test_Property')
        self.type_of_flag = FlagType.objects.create(flag_type_name='test_flag')
        self.flag_raised_by = User.objects.create(username="bob")
        self.message = 'This property is mine'

        self.property1 = Property.objects.create(property_title='test_Prop1')
        self.type_of_flag1 = FlagType.objects.create(flag_type_name='flag1')
        self.flag_raised_by1 = User.objects.create(username="bob1")

        self.flagged_property = FlaggedProperty.objects.create(
            property=self.property,
            type_of_flag=self.type_of_flag,
            flag_raised_by=self.flag_raised_by,
            message=self.message
        )

        self.data = {
            'property': reverse('property-detail',
                                args=[self.property1.id]),
            'type_of_flag': reverse('flagtype-detail',
                                    args=[self.type_of_flag1.id]),
            'flag_raised_by': reverse('user-detail',
                                      args=[self.flag_raised_by1.id]),
            'message': ' updated_test_message',
        }

    def test_can_update_flagged_property(self):
        response = self.client.put(reverse('flaggedproperty-detail',
                                           args=[self.flagged_property.id]),
                                   self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteFlaggedPropertyTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.property = Property.objects.create(property_title='test_Property')
        self.type_of_flag = FlagType.objects.create(flag_type_name='test_flag')
        self.flag_raised_by = User.objects.create(username="bob")
        self.message = 'This property is mine'

        self.flagged_property = FlaggedProperty.objects.create(
            property=self.property,
            type_of_flag=self.type_of_flag,
            flag_raised_by=self.flag_raised_by,
            message=self.message
        )

    def test_can_delete_flagged_property(self):
        response = self.client.delete(reverse('flaggedproperty-detail',
                                              args=[self.flagged_property.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
