from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.request import Request

from properties.serializers import *
from rest_framework.test import APIRequestFactory
from .models import *
from django.core.files.base import File
import tempfile

factory = APIRequestFactory()
request = factory.get('/')
serializer_context = {
    'request': Request(request),
}


class CreatePropertyTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.data = {'user': reverse('user-detail', args=[self.user.id]), 'property_title': 'New Homes in Las Vegas NV'}

    def test_can_create_property(self):
        response = self.client.post(reverse('property-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadPropertyTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.property = Property.objects.create(user=self.user, property_title='New Homes in Las Vegas NV')

    def test_can_read_property_list(self):
        response = self.client.get(reverse('property-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_property_detail(self):
        response = self.client.get(reverse('property-detail', args=[self.property.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdatePropertyTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.property = Property.objects.create(user=self.user, property_title='New Homes in Las Vegas NV')
        self.data = PostPropertySerializer(self.property, context=serializer_context).data
        self.data.update({'address': 'Kharadi'})
        self.data.pop('user')

    def test_can_update_property(self):
        response = self.client.put(reverse('property-detail', args=[self.property.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeletePropertyTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.property = Property.objects.create(user=self.user, property_title='New Homes in Las Vegas NV')

    def test_can_delete_property(self):
        response = self.client.delete(reverse('property-detail', args=[self.property.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateShortlistedPropertyTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.property = Property.objects.create(user=self.user, property_title='New Homes in Las Vegas NV')
        self.data = {'user': reverse('user-detail', args=[self.user.id]),
                     'property': reverse('property-detail', args=[self.property.id])}

    def test_can_create_shortlisted_property(self):
        response = self.client.post(reverse('shortlistedproperty-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadShortlistedPropertyTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.property = Property.objects.create(user=self.user, property_title='New Homes in Las Vegas NV')
        self.shortlisted_property = ShortListedProperty.objects.create(property=self.property, user=self.user)

    def test_can_read_shortlisted_property_list(self):
        response = self.client.get(reverse('shortlistedproperty-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_shortlisted_property_detail(self):
        response = self.client.get(reverse('shortlistedproperty-detail', args=[self.shortlisted_property.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteShortlistedPropertyTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.property = Property.objects.create(user=self.user, property_title='New Homes in Las Vegas NV')
        self.shortlisted_property = ShortListedProperty.objects.create(property=self.property, user=self.user)

    def test_can_delete_shortlisted_property(self):
        response = self.client.delete(reverse('shortlistedproperty-detail', args=[self.property.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ReadRecommendedPropertyTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.property1 = Property.objects.create(user=self.user, property_title='New Homes in Las Vegas NV',
                                                city="NV", property_value=12312)
        self.property2 = Property.objects.create(user=self.user, property_title='New Homes in Las Vegas NV',
                                                 city="NV", property_value=12332)

    def test_can_read_recommended_property_list(self):
        response = self.client.get('/api/recommended_properties/?id=' + str(self.property1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Test cases for Property Status API

class CreatePropertyStatusTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.data = {'status': 'test_property_status'}

    def test_can_create_property(self):
        response = self.client.post(reverse('propertystatus-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadPropertyStatusTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.propertystatus = PropertyStatus.objects.create(status='test_status')

    def test_can_read_property_list(self):
        response = self.client.get(reverse('propertystatus-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_property_detail(self):
        response = self.client.get(reverse('propertystatus-detail', args=[self.propertystatus.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Test cases for Images API

# class CreateImageTest(APITestCase):
#
#     def setUp(self):
#         self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
#         self.client.login(username='john', password='johnpassword')
#         self.user = User.objects.create(username="mike")
#         tmp_file = File(file=tempfile.NamedTemporaryFile(suffix='.jpg'))
#         self.data = {'image': tmp_file}
#
#     def test_can_create_image(self):
#         response = self.client.post(reverse('images-list'), self.data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# class ReadImageTest(APITestCase):
#     def setUp(self):
#         self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
#         self.client.login(username='john', password='johnpassword')
#         self.user = User.objects.create(username="mike")
#         img = Image.new('RGB', (100, 100))
#         tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
#         img.save(tmp_file)
#         self.image = Images.objects.create(image=tmp_file)
#
#     def test_can_read_image_list(self):
#         response = self.client.get(reverse('images-list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_read_image_detail(self):
#         response = self.client.get(reverse('images-detail', args=[self.image.id]))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#
# class DeleteImageTest(APITestCase):
#     def setUp(self):
#         self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
#         self.client.login(username='john', password='johnpassword')
#         self.user = User.objects.create(username="mike")
#         img = Image.new('RGB', (100, 100))
#         tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
#         img.save(tmp_file)
#         self.image = Images.objects.create(image=tmp_file)
#
#     def test_can_delete_image(self):
#         response = self.client.delete(reverse('images-detail', args=[self.image.id]))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
