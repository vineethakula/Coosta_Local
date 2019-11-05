from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.request import Request

from properties.models import Property
from appointments.models import OpenHouse, OpenHouseRSVP, OwnerAvailability, AppointmentRequest
from rest_framework.test import APIRequestFactory
from django.utils import timezone

factory = APIRequestFactory()
request = factory.get('/')
serializer_context = {
    'request': Request(request),
}


class CreateOpenHouseTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.property = Property.objects.create(property_title='test_Property')
        self.date = timezone.now()
        self.start_time = timezone.now()
        self.end_time = timezone.now()

        self.data = {
            'property': reverse('property-detail', args=[self.property.id]),
            'date': self.date,
            'start_date': self.start_time,
            'end_date': self.end_time
        }

    def test_can_create_openhouse(self):
        response = self.client.post(reverse('openhouse-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadOpenHouseTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.property = Property.objects.create(property_title='test_Property')
        self.date = timezone.now()
        self.start_time = timezone.now()
        self.end_time = timezone.now()

        self.openhouse = OpenHouse.objects.create(property=self.property,
                                                  date=self.date,
                                                  start_time=self.start_time,
                                                  end_time=self.end_time)

    def test_can_read_openhouse_list(self):
        response = self.client.get(reverse('openhouse-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_openhouse_detail(self):
        response = self.client.get(reverse('openhouse-detail',
                                           args=[self.openhouse.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateOpenHouseTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.property = Property.objects.create(property_title='test_Property')
        self.property2 = Property.objects.create(property_title='test_Prop2')
        self.date = timezone.now()
        self.start_time = timezone.now()
        self.end_time = timezone.now()

        self.openhouse = OpenHouse.objects.create(property=self.property,
                                                  date=self.date,
                                                  start_time=self.start_time,
                                                  end_time=self.end_time)

        self.data = {
            'property': reverse('property-detail', args=[self.property2.id]),
            'date': self.date,
            'start_date': self.start_time,
            'end_date': self.end_time
        }

    def test_can_update_openhouse(self):
        response = self.client.put(reverse('openhouse-detail',
                                           args=[self.openhouse.id]),
                                   self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteOpenHouseTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.property = Property.objects.create(property_title='test_Property')
        self.date = timezone.now()
        self.start_time = timezone.now()
        self.end_time = timezone.now()

        self.openhouse = OpenHouse.objects.create(property=self.property,
                                                  date=self.date,
                                                  start_time=self.start_time,
                                                  end_time=self.end_time)

    def test_can_delete_openhouse(self):
        response = self.client.delete(reverse('openhouse-detail',
                                              args=[self.openhouse.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateOpenHouseRSVPTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.test_user = User.objects.create(username="bob")
        self.property = Property.objects.create(property_title='test_Property')
        self.date = timezone.now()
        self.start_time = timezone.now()
        self.end_time = timezone.now()

        self.openhouse = OpenHouse.objects.create(property=self.property,
                                                  date=self.date,
                                                  start_time=self.start_time,
                                                  end_time=self.end_time)

        self.data = {
            'open_house': reverse('openhouse-detail',
                                  args=[self.openhouse.id]),
            'rsvp_user': reverse('user-detail', args=[self.test_user.id]),
        }

    def test_can_create_openhousersvp(self):
        response = self.client.post(reverse('openhousersvp-list'), self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadOpenHouseRSVPTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.test_user = User.objects.create(username="bob")
        self.property = Property.objects.create(property_title='test_Property')
        self.date = timezone.now()
        self.start_time = timezone.now()
        self.end_time = timezone.now()

        self.openhouse = OpenHouse.objects.create(property=self.property,
                                                  date=self.date,
                                                  start_time=self.start_time,
                                                  end_time=self.end_time)

        self.openhousersvp = OpenHouseRSVP.objects.create(
            open_house=self.openhouse,
            rsvp_user=self.test_user
        )

    def test_can_read_openhousersvp_list(self):
        response = self.client.get(reverse('openhousersvp-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_openhousersvp_detail(self):
        response = self.client.get(reverse('openhousersvp-detail',
                                           args=[self.openhousersvp.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateOpenHouseRSVPTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.test_user1 = User.objects.create(username="bob")
        self.test_user2 = User.objects.create(username="thebuilder")
        self.property1 = Property.objects.create(property_title='lohegaon')
        self.property2 = Property.objects.create(property_title='wagholi')
        self.date = timezone.now()
        self.start_time = timezone.now()
        self.end_time = timezone.now()

        self.openhouse1 = OpenHouse.objects.create(property=self.property1,
                                                   date=self.date,
                                                   start_time=self.start_time,
                                                   end_time=self.end_time)

        self.openhouse2 = OpenHouse.objects.create(property=self.property2,
                                                   date=self.date,
                                                   start_time=self.start_time,
                                                   end_time=self.end_time)

        self.openhousersvp = OpenHouseRSVP.objects.create(
            open_house=self.openhouse1,
            rsvp_user=self.test_user1
        )

        self.data = {
            'open_house': reverse('openhouse-detail',
                                  args=[self.openhouse2.id]),
            'rsvp_user': reverse('user-detail',
                                 args=[self.test_user2.id])
        }

    def test_can_update_openhousersvp(self):
        response = self.client.put(reverse('openhousersvp-detail',
                                           args=[self.openhousersvp.id]),
                                   self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteOpenHouseRSVPTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.test_user1 = User.objects.create(username="bob")
        self.property1 = Property.objects.create(property_title='lohegaon')
        self.date = timezone.now()
        self.start_time = timezone.now()
        self.end_time = timezone.now()

        self.openhouse1 = OpenHouse.objects.create(property=self.property1,
                                                   date=self.date,
                                                   start_time=self.start_time,
                                                   end_time=self.end_time)

        self.openhousersvp = OpenHouseRSVP.objects.create(
            open_house=self.openhouse1,
            rsvp_user=self.test_user1
        )

    def test_can_delete_openhousersvp(self):
        response = self.client.delete(reverse('openhousersvp-detail',
                                              args=[self.openhousersvp.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateOwnerAvailabilityTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.property = Property.objects.create(property_title='test_Property')
        self.wkd_start_time = timezone.now().time()
        self.wkd_end_time = timezone.now().time()

        self.data = {
            'property': reverse('property-detail', args=[self.property.id]),
            'wkd_start_date': self.wkd_start_time,
            'wkd_end_date': self.wkd_end_time
        }

    def test_can_create_owneravailability(self):
        response = self.client.post(reverse('owneravailability-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadOwnerAvailabilityTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.property = Property.objects.create(property_title='test_Property')
        self.wkd_start_time = timezone.now().time()
        self.wkd_end_time = timezone.now().time()

        self.owneravailability = OwnerAvailability.objects.create(property=self.property,
                                                                  wkd_start_time=self.wkd_start_time,
                                                                  wkd_end_time=self.wkd_end_time)

    def test_can_read_owneravailability_list(self):
        response = self.client.get(reverse('owneravailability-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_owneravailability_detail(self):
        response = self.client.get(reverse('owneravailability-detail',
                                           args=[self.owneravailability.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateOwnerAvailabilityTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.property = Property.objects.create(property_title='test_Property')
        self.property2 = Property.objects.create(property_title='test_Prop2')
        self.wkd_start_time = timezone.now().time()
        self.wkd_end_time = timezone.now().time()

        self.owneravailability = OwnerAvailability.objects.create(property=self.property,
                                                                  wkd_start_time=self.wkd_start_time,
                                                                  wkd_end_time=self.wkd_end_time)

        self.data = {
            'property': reverse('property-detail', args=[self.property2.id]),
            'wkd_start_date': self.wkd_start_time,
            'wkd_end_date': self.wkd_end_time
        }

    def test_can_update_owneravailability(self):
        response = self.client.put(reverse('owneravailability-detail',
                                           args=[self.owneravailability.id]),
                                   self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteOwnerAvailabilityTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.property = Property.objects.create(property_title='test_Property')
        self.wkd_start_time = timezone.now().time()
        self.wkd_end_time = timezone.now().time()

        self.owneravailability = OwnerAvailability.objects.create(property=self.property,
                                                                  wkd_start_time=self.wkd_start_time,
                                                                  wkd_end_time=self.wkd_end_time)

    def test_can_delete_owneravailability(self):
        response = self.client.delete(reverse('owneravailability-detail',
                                              args=[self.owneravailability.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateAppointmentRequestTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.test_user = User.objects.create(username="bob")
        self.property = Property.objects.create(property_title='test_Property')
        self.wkd_start_time = timezone.now().time()
        self.wkd_end_time = timezone.now().time()
        self.requested_time = timezone.now().time()
        self.requested_date = timezone.now().date()

        self.owneravailability = OwnerAvailability.objects.create(property=self.property,
                                                                  wkd_start_time=self.wkd_start_time,
                                                                  wkd_end_time=self.wkd_end_time)

        self.data = {
            'owner_availability': reverse('owneravailability-detail', args=[self.owneravailability.id]),
            'buyer': reverse('user-detail', args=[self.test_user.id]),
            'requested_time': self.requested_time,
            'requested_date': self.requested_date
        }

    def test_can_create_appointmentrequest(self):
        response = self.client.post(reverse('appointmentrequest-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadAppointmentRequestTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.test_user = User.objects.create(username="bob")
        self.property = Property.objects.create(property_title='test_Property')
        self.wkd_start_time = timezone.now().time()
        self.wkd_end_time = timezone.now().time()
        self.requested_time = timezone.now().time()
        self.requested_date = timezone.now().date()

        self.owneravailability = OwnerAvailability.objects.create(property=self.property,
                                                                  wkd_start_time=self.wkd_start_time,
                                                                  wkd_end_time=self.wkd_end_time)

        self.appointmentrequest = AppointmentRequest.objects.create(owner_availability=self.owneravailability,
                                                                    buyer=self.test_user,
                                                                    requested_time=self.requested_time,
                                                                    requested_date= self.requested_date)

    def test_can_read_appointmentrequest_list(self):
        response = self.client.get(reverse('appointmentrequest-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_appointmentrequest_detail(self):
        response = self.client.get(reverse('appointmentrequest-detail',
                                           args=[self.appointmentrequest.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateAppointmentRequestTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.test_user1 = User.objects.create(username="bob")
        self.test_user2 = User.objects.create(username="marley")
        self.property1 = Property.objects.create(property_title='test_property1')
        self.property2 = Property.objects.create(property_title='test_property2')
        self.wkd_start_time = timezone.now().time()
        self.wkd_end_time = timezone.now().time()
        self.requested_time = timezone.now().time()
        self.requested_date = timezone.now().date()

        self.owneravailability1 = OwnerAvailability.objects.create(property=self.property1,
                                                                   wkd_start_time=self.wkd_start_time,
                                                                   wkd_end_time=self.wkd_end_time)

        self.owneravailability2 = OwnerAvailability.objects.create(property=self.property2,
                                                                  wkd_start_time=self.wkd_start_time,
                                                                  wkd_end_time=self.wkd_end_time)

        self.appointmentrequest = AppointmentRequest.objects.create(owner_availability=self.owneravailability1,
                                                                    buyer=self.test_user1,
                                                                    requested_time=self.requested_time,
                                                                    requested_date=self.requested_date)

        self.data = {
            'owner_availability': reverse('owneravailability-detail', args=[self.owneravailability2.id]),
            'buyer': reverse('user-detail', args=[self.test_user2.id]),
            'requested_time': self.requested_time,
            'requested_date': self.requested_date
        }

    def test_can_update_appointmentrequest(self):
        response = self.client.put(reverse('appointmentrequest-detail',
                                           args=[self.appointmentrequest.id]),
                                   self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteAppointmentRequestTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.test_user = User.objects.create(username="bob")
        self.property = Property.objects.create(property_title='lohegaon')
        self.wkd_start_time = timezone.now().time()
        self.wkd_end_time = timezone.now().time()
        self.requested_time = timezone.now().time()
        self.requested_date = timezone.now().date()

        self.owneravailability = OwnerAvailability.objects.create(property=self.property,
                                                                  wkd_start_time=self.wkd_start_time,
                                                                  wkd_end_time=self.wkd_end_time)

        self.appointmentrequest = AppointmentRequest.objects.create(owner_availability=self.owneravailability,
                                                                    buyer=self.test_user,
                                                                    requested_time=self.requested_time,
                                                                    requested_date=self.requested_date)

    def test_can_delete_appointmentrequest(self):
        response = self.client.delete(reverse('appointmentrequest-detail',
                                              args=[self.appointmentrequest.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)