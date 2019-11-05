from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework import filters
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
import requests
from rest_framework.parsers import MultiPartParser, FormParser
import xmltodict
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import urllib
from urlparse import urlparse
from django.core.files import File
from django.db.models import Q
from django.conf import settings
from drf_custom_viewsets.viewsets import CustomSerializerViewSet

RECOMMENDED_PROPERTY_VALUE_RANGE = 2000 #FixMe: Move this this to configuration ( may be settings )


class PropertyStatusViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = PropertyStatus.objects.all()
    serializer_class = PropertyStatusSerializer


class PropertyViewSet(CustomSerializerViewSet):
    """
    API endpoint that allows Property to be viewed or edited.
    """
    permission_classes = (AllowAny,)
    queryset = Property.objects.all().order_by('-listed_on')
    serializer_class = GetPropertySerializer
    custom_serializer_classes = {
        'create': PostPropertySerializer,
        'update': PostPropertySerializer,
    }
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('property_value', 'property_size', 'listed_on', 'completed')
    filter_fields = {
            'search_index': ['icontains'],
            'address': ['icontains'],
            'id': ['lte', 'gte'],
            'property_value': ['lte', 'gte'],
            'beds': ['lte', 'gte'],
            'baths': ['lte', 'gte'],
            'property_size': ['lte', 'gte'],
            'city':['icontains'],
            'state':['icontains'],
            'zip_code':['icontains'],
            'user': ['exact'],
            'home_type': ['icontains'],
            'completed': ['exact']
        }


class RecommendedPropertyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Recommended properties to be viewed.
    """
    permission_classes = (AllowAny,)
    serializer_class = GetPropertySerializer

    @list_route()
    def get_queryset(self):
        """
        This view should return a list of all the recommended property.
        """
        property_id = self.request.query_params.get('id', None)
        property = Property.objects.get(id=property_id)
        min_cos = property.property_value - 2000
        if not min_cos >= 0:
            min_cos = 0
        shortlisted_property = ShortListedProperty.objects.filter(user=
                                                                  self.request.user).values('property__id')
        shortlisted_property_id = [shortlisted_property[x]['property__id'] for x
                                   in xrange(0, len(shortlisted_property))]

        queryset =  Property.objects.filter(Q(city__contains=property.city, property_value__gt=min_cos,
                                                                                property_value__lt=
                                                                                property.property_value + 2000))\
            .exclude(id=property.id).exclude(id__in=shortlisted_property_id).order_by('-listed_on')
        return queryset


class PropertyImagesViewSet(CustomSerializerViewSet):
    """
    API endpoint that allows Property Images to be viewed or edited.
    """
    permission_classes = (AllowAny,)
    queryset = PropertyImages.objects.all()
    serializer_class = GetPropertyImagesSerializer
    custom_serializer_classes = {
        'create': PostPropertyImagesSerializer,
        'update': PostPropertyImagesSerializer,
    }
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('image', 'property')
    filter_fields = {
            'property': ['exact'],
            'image': ['exact'],
        }


class ImagesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows All Images to be viewed or edited.
    """
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(image=self.request.data.get('file'))


class ShortlistedPropertyViewSet(CustomSerializerViewSet):
    """
    API endpoint that allows Property to be viewed or edited.
    """
    permission_classes = (AllowAny,)
    queryset = ShortListedProperty.objects.all().order_by('-shortlisted_on')
    serializer_class = GetShortListedPropertySerializer
    custom_serializer_classes = {
        'create': PostShortListedPropertySerializer,
        'update': PostShortListedPropertySerializer,
    }
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('user', 'property')
    filter_fields = {
            'user': ['exact'],
            'property': ['exact'],
        }


class ParcelViewSet(CustomSerializerViewSet):
    """
    API endpoint that allows Property to be viewed or edited.
    """
    permission_classes = (AllowAny,)
    queryset = Parcel.objects.all().order_by('-id')
    serializer_class = ParcelSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('AIN', 'AssessorID', 'YearBuilt')


class ZillowAPIView(APIView):

    def get(self, request, address=None, city=None, state=None):
        # Process any get params that you may need
        # If you don't need to process get params,
        # you can skip this part
        # address = request.GET.get('arg1', None)
        # city = request.GET.get('arg2', None)
        # state = request.GET.get('arg3', None)
        #
        # # Any URL parameters get passed in **kw
        zillow_property = zillow_offline_api(address.replace("_", " "), city.replace("_", " "), state.replace("_", " "))
        response = Response(zillow_property, status=status.HTTP_200_OK)
        return response


@login_required(login_url='/user/login/')
def property_list(request):
    address, city, state = "", "", ""
    if request.method == "POST":
        address = request.POST.get("address", "").replace(", United States", "").strip()
        city = request.POST.get("city", "").strip()
        state = request.POST.get("stateSelection", "").strip()
        if address and city:
            search_address = address + ", " + city + ", " + state
        elif not address and city:
            search_address = city + ", " + state
        if address and city:
            try:
                property = Property.objects.filter(address__icontains=address, city__icontains=city,
                                                   state__icontains=state)
                if not property:
                    zillow_property = zillow_offline_api(address, city, state)
                    if not "Error" in zillow_property:
                        for z_p in zillow_property:
                            zpid = z_p.pop('zpid', None)
                            u = User.objects.get_or_create(username="zillow")[0]
                            u.set_password('zilLow@321')
                            u.save()
                            z_p['user'] = u
                            property, created = Property.objects.get_or_create(**z_p)
                            if created:
                                zpid_data = zillow_zpid_detail(zpid)
                                if not "Error" in zpid_data:
                                    # TODO save detail and image
                                    try:
                                        property.description = zpid_data['description']
                                    except:
                                        pass
                                    try:
                                        photo = Images()  # set any other fields, but don't commit to DB (ie. don't save())
                                        name = urlparse(zpid_data['image']).path.split('/')[-1]
                                        content = urllib.urlretrieve(zpid_data['image'], settings.MEDIA_ROOT)
                                        photo.image.save(name, File(open(content[0])), save=True)
                                        PropertyImages.objects.create(property=property, image=photo)
                                    except:
                                        pass
                            property.search_index = property.address.strip() + ", " + property.city.strip() \
                                                    + ", " + property.state.strip() + " " \
                                                    + property.zip_code.strip()
                            property.save()
                            if len(zillow_property) == 1:
                                return HttpResponseRedirect("/property/preview/" + str(property.id))
            except:
                return render(request, 'home_page.html',
                              {'error': "please use proper address or use suggestion in dropdown as help."})


    return render(request, 'property/property_list.html', {"address": address, "city": city, "state": state})

@login_required(login_url='/user/login/')
def property_detail_page(request, property_id):
    """ """
    property_id = property_id
    try:
        p = Property.objects.get(id=property_id, user=request.user)
        my_pro_flag = True
    except:
        my_pro_flag = False
    return render(request, 'property/property_detail_page.html', {'property_id':property_id,
                                                                  'my_pro_flag': my_pro_flag})

@login_required(login_url='/user/login/')
def my_shortlisted_property(request):
    return render(request, 'property/my_shortlisted_property.html')


@login_required(login_url='/user/login/')
def my_property(request, property_id=0):
    # user = request.user
    # if user.is_authenticated:
    property_id = property_id

    if property_id == 0:
        return render(request, 'property/my_property.html')
    else:
        try:
            p = Property.objects.get(id=property_id, user=request.user)
            return render(request, 'property/edit_property.html', {'property_id': p.id})
        except:
            try:
                user = User.objects.filter(username='zillow')
                p2 = Property.objects.get(id=property_id, user=user)
                return render(request, 'property/edit_property.html', {'property_id': p2.id})
            except:
                raise Exception(403, "Permission Denied")


@login_required(login_url='/user/login/')
def add_property(request):
    return render(request, 'property/add_property.html')


@login_required(login_url='/user/login/')
def home_page(request):
    return render(request, 'home_page.html')


def zillow_offline_api(address, city, state):
    """ """
    address = address.strip() + ' ' + city.strip()
    url = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm'
    parameters = {'zws-id': "X1-ZWz19lq7ppy70r_305s0",
                  'address': address,
                  'citystatezip': state
                  }
    resp = requests.get(url, params=parameters)
    data = resp.content.decode('utf-8')
    xmltodict_data = xmltodict.parse(data)
    if not "Error" in xmltodict_data.get('SearchResults:searchresults', None)['message']['text']:
        rst = xmltodict_data.get('SearchResults:searchresults', None)['response']['results']
        output = []
        if type(rst['result']) == list:
            rst_objects = []
            for obj in rst['result']:
                rst_objects.append(dict(obj))
        else:
            rst_objects = [dict(rst['result'])]
        # links = dict(rst['links'])
        # results_dct['links'] = links
        for rst_obj in rst_objects:
            results_dct = {}
            address = dict(rst_obj['address'])
            results_dct['address'] = address
            try:
                results_dct['year_built'] = rst_obj['yearBuilt']
            except:
                pass
            try:
                results_dct['property_value'] = int(dict(dict(rst_obj['zestimate'])['amount'])['#text'])
            except:
                pass
            # value_change = dict(dict(rst['zestimate'])['valueChange'])['#text']
            # results_dct['value_change'] = value_change
            # value_change_duration = dict(dict(rst['zestimate'])['valueChange'])['@duration']
            # valuationRangeLow = dict(dict(dict(rst['zestimate'])['valuationRange'])['low'])['#text']
            # valuationRangeHigh = dict(dict(dict(rst['zestimate'])['valuationRange'])['high'])['#text']
            # vluation_text = "Valuation Change in last %s days - High: %s Low: %s" % (
            # value_change_duration, valuationRangeHigh, valuationRangeLow)
            # results_dct['vluation_text'] = vluation_text
            try:
                results_dct['baths'] = int(float(rst_obj['bathrooms']))
            except:
                results_dct['baths'] = 0
            try:
                results_dct['home_type'] = rst_obj['useCode']
            except:
                pass
            try:
                results_dct['beds'] = int(rst_obj['bedrooms'])
            except:
                results_dct['beds'] = 0
            try:
                results_dct['rooms'] = int(rst_obj['totalRooms'])
            except:
                results_dct['rooms'] = 0
                pass
            # results_dct['lotSizeSqFt'] = rst_obj['lotSizeSqFt']
            try:
                results_dct['property_size'] = int(rst_obj['finishedSqFt'])
            except:
                results_dct['property_size'] = 0
            results_dct['city'] = address['city']
            results_dct['state'] = address['state']
            results_dct['latitude'] = address['latitude']
            results_dct['longitude'] = address['longitude']
            results_dct['zip_code'] = address['zipcode']
            results_dct['address'] = address['street']
            try:
                results_dct['zpid'] = rst_obj['zpid']
            except:
                results_dct['zpid'] = 0
            output.append(results_dct)
        return output
    else:
        return xmltodict_data.get('SearchResults:searchresults', None)['message']['text']


def zillow_zpid_detail(zpid):
    url = 'http://www.zillow.com/webservice/GetUpdatedPropertyDetails.htm'
    parameters = {'zws-id': "X1-ZWz19lq7ppy70r_305s0",
                  'zpid': zpid
                  }
    resp = requests.get(url, params=parameters)
    data = resp.content.decode('utf-8')
    xmltodict_data = xmltodict.parse(data)
    detail_dict = {}
    if not "Error" in xmltodict_data.get('UpdatedPropertyDetails:updatedPropertyDetails', None)['message']['text']:
        try:
            rst = dict(xmltodict_data.get('UpdatedPropertyDetails:updatedPropertyDetails', None)['response'])
        except:
            pass
        try:
            detail_dict['image'] = rst['images'].get('image').get('url')
        except:
            pass
        try:
            detail_dict['description'] = "\n".join([x + ": " + rst['editedFacts'].get(x) + "" for x in list(rst['editedFacts'])])
        except:
            pass
        return detail_dict
    else:
        return xmltodict_data.get('UpdatedPropertyDetails:updatedPropertyDetails', None)['message']['text']


def is_address(address):
    """ """
    address = address.split(' ')
    if address[0].isdigit():
        return True
    return False


def pull_growth_hack_properties():
    import requests

    headers = {'content-type': 'application/json', 'method': 'crawler.pull_zillow_property_for_coosta'}
    url = 'http://ec2-52-39-52-71.us-west-2.compute.amazonaws.com:8000/api'

    data = requests.get(url, headers=headers)
    return data


@login_required(login_url='/user/login/')
def property_preview_page(request, property_id):
    """ """
    property_id = property_id
    try:
        p = Property.objects.get(id=property_id, user=request.user)
        return render(request, 'property/property_preview.html', {'property_id': p.id})
    except:
        raise Exception(403, "Permission Denied")
