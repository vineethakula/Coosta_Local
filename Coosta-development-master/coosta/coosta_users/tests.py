from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.request import Request

from coosta_users.serializers import *
from rest_framework.test import APIRequestFactory
from .models import UserProfile, NonPreApprovedUser, PreApprovedUser, Documents

factory = APIRequestFactory()
request = factory.get('/')
serializer_context = {
    'request': Request(request),
}

class CreateUserTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.data = {'username': 'mike', 'first_name': 'Mike', 'last_name': 'Tyson', 'password': 'hellomike'}

    def test_can_create_user(self):
        response = self.client.post(reverse('user-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadUserTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")

    def test_can_read_user_list(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_user_detail(self):
        response = self.client.get(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateUserTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike", first_name="Tyson", password="mtyson")
        self.data = UserSerializer(self.user, context=serializer_context).data
        self.data.pop('userprofile')
        self.data.update({'first_name': 'Changed'})

    def test_can_update_user(self):
        response = self.client.put(reverse('user-detail', args=[self.user.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteUserTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mikey")

    def test_can_delete_user(self):
        response = self.client.delete(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


#User Profile Test Cases

class CreateUserProfileTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.data = {'user': reverse('user-detail', args=[self.user.id]), 'area_code': '020', 'mobile_number': '7030999223',
                     'address': 'Kharadi', 'city': 'Pune', 'town': 'Pune', 'state': 'Maharashtra',
                     'zip_code': '411014'}

    def test_can_create_user_profile(self):
        response = self.client.post(reverse('userprofile-list'), self.data)
        self.assertEqual(response.status_code, 400)


class ReadUserProfileTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.userprofile = UserProfile.objects.get(user=self.user)
        self.userprofile.city = "Pune"
        self.userprofile.save()

    def test_can_read_user_profile_list(self):
        response = self.client.get(reverse('userprofile-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_user_profile_detail(self):
        response = self.client.get(reverse('userprofile-detail', args=[self.userprofile.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateUserProfileTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.userprofile = UserProfile.objects.get(user=self.user)
        self.userprofile.city = "Pune"
        self.userprofile.save()
        self.data = UserProfileSerializer(self.userprofile, context=serializer_context).data
        self.data.pop('profile_image')
        self.data.update({'city': 'Patna'})

    def test_can_update_user_profile(self):
        response = self.client.put(reverse('userprofile-detail', args=[self.userprofile.id]), self.data,
                                   format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteUserTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.userprofile = UserProfile.objects.get(user=self.user)
        self.userprofile.city = "Pune"
        self.userprofile.save()

    def test_can_delete_user_profile(self):
        response = self.client.delete(reverse('userprofile-detail', args=[self.userprofile.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


#Non-Pre-Approved User Test Case
class CreateNonPreApprovedUserTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.user = User.objects.create(username="mike")

        self.data = {
            'user': reverse('user-detail', args=[self.user.id])
        }

    def test_can_create_non_pre_approved_user(self):
        response = self.client.post(reverse('non_pre_approved_user-list'), self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadNonPreApprovedUserTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.user = User.objects.create(username="mike")
        self.non_pre_approved_user = NonPreApprovedUser.objects.create(user=self.user)

    def test_can_read_non_pre_approved_user_list(self):
        response = self.client.get(reverse('non_pre_approved_user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_non_pre_approved_user_detail(self):
        response = self.client.get(reverse('non_pre_approved_user-detail', args=[self.non_pre_approved_user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateNonPreApprovedUserTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.user = User.objects.create(username="mike")
        self.non_pre_approved_user = NonPreApprovedUser.objects.create(user=self.user)

        self.data = {
            'user': reverse('user-detail', args=[self.non_pre_approved_user.id])
        }

    def test_can_update_non_pre_approved_user(self):
        response = self.client.put(reverse('non_pre_approved_user-detail',
                                           args=[self.non_pre_approved_user.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteNonPreApprovedUserTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.user = User.objects.create(username="mike")
        self.non_pre_approved_user = NonPreApprovedUser.objects.create(user=self.user)

    def test_can_delete_non_pre_approved_user(self):
        response = self.client.delete(reverse('non_pre_approved_user-detail',
                                              args=[self.non_pre_approved_user.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


#Pre-Approved User Test Case
class CreatePreApprovedUserTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.user = User.objects.create(username="mike")

        self.data = {
            'user': reverse('user-detail', args=[self.user.id])
        }

    def test_can_create_pre_approved_user(self):
        response = self.client.post(reverse('pre_approved_user-list'), self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadPreApprovedUserTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.user = User.objects.create(username="mike")
        self.pre_approved_user = PreApprovedUser.objects.create(user=self.user)

    def test_can_read_pre_approved_user_list(self):
        response = self.client.get(reverse('pre_approved_user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_pre_approved_user_detail(self):
        response = self.client.get(reverse('pre_approved_user-detail', args=[self.pre_approved_user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdatePreApprovedUserTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.user = User.objects.create(username="mike")
        self.pre_approved_user = PreApprovedUser.objects.create(user=self.user)

        self.data = {
            'user': reverse('user-detail', args=[self.pre_approved_user.id])
        }

    def test_can_update_pre_approved_user(self):
        response = self.client.put(reverse('pre_approved_user-detail',
                                           args=[self.pre_approved_user.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeletePreApprovedUserTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.user = User.objects.create(username="mike")
        self.pre_approved_user = PreApprovedUser.objects.create(user=self.user)

    def test_can_delete_non_pre_approved_user(self):
        response = self.client.delete(reverse('pre_approved_user-detail',
                                              args=[self.pre_approved_user.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# Test cases for Documents API

class CreateDocumentsTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.data = {}

    def test_can_create_documents(self):
        response = self.client.post(reverse('documents-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadDocumentsTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.document = Documents.objects.create()

    def test_can_read_document_list(self):
        response = self.client.get(reverse('documents-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_documents_detail(self):
        response = self.client.get(reverse('documents-detail', args=[self.document.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteImageTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.user = User.objects.create(username="mike")
        self.document = Documents.objects.create()

    def test_can_delete_documents(self):
        response = self.client.delete(reverse('documents-detail', args=[self.document.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

