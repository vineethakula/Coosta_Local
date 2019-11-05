from rest_framework import viewsets
from statistic.serializers import PageViewSerializer, PageViewCountSerializer
from statistic.models import PageView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from properties.models import *
import json
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt


class PageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = PageView.objects.all().order_by('-viewed_on')
    serializer_class = PageViewSerializer


class GetPropertyPageViewCount(GenericAPIView):
    serializer_class = PageViewCountSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, property_id):
        property_views = PageView.objects.filter(property__id=property_id).count()
        # TODO: This len call is deadly
        # Fixed by @mallikdav by removing len and adding count() method
        response = Response(property_views, status=status.HTTP_200_OK)
        return response


@login_required(login_url='/user/login/')
@csrf_exempt
def statistics_home(request):
    user_properties = Property.objects.filter(user=request.user)
    user_properties_id = [property.id for property in user_properties]
    today = datetime.today()
    week_1_start = datetime.today() - timedelta(days=7)
    week_2_start = datetime.today() - timedelta(days=14)
    week_3_start = datetime.today() - timedelta(days=21)
    week_4_start = datetime.today() - timedelta(days=28)
    week_5_start = datetime.today() - timedelta(days=35)
    views1 = PageView.objects.filter(property__id__in=user_properties_id, viewed_on__gte=week_1_start,
                                     viewed_on__lte=today).count()
    views2 = PageView.objects.filter(property__id__in=user_properties_id, viewed_on__gte=week_2_start,
                                     viewed_on__lte=week_1_start).count()
    views3 = PageView.objects.filter(property__id__in=user_properties_id, viewed_on__gte=week_3_start,
                                     viewed_on__lte=week_2_start).count()
    views4 = PageView.objects.filter(property__id__in=user_properties_id, viewed_on__gte=week_4_start,
                                     viewed_on__lte=week_3_start).count()
    views5 = PageView.objects.filter(property__id__in=user_properties_id, viewed_on__gte=week_5_start,
                                     viewed_on__lte=week_4_start).count()
    shortlist1 = ShortListedProperty.objects.filter(property__id__in=user_properties_id,
                                                    shortlisted_on__gte=week_1_start,
                                                    shortlisted_on__lte=today).count()
    shortlist2 = ShortListedProperty.objects.filter(property__id__in=user_properties_id,
                                                    shortlisted_on__gte=week_2_start,
                                                    shortlisted_on__lte=week_1_start).count()
    shortlist3 = ShortListedProperty.objects.filter(property__id__in=user_properties_id,
                                                    shortlisted_on__gte=week_3_start,
                                                    shortlisted_on__lte=week_2_start).count()
    shortlist4 = ShortListedProperty.objects.filter(property__id__in=user_properties_id,
                                                    shortlisted_on__gte=week_4_start,
                                                    shortlisted_on__lte=week_3_start).count()
    shortlist5 = ShortListedProperty.objects.filter(property__id__in=user_properties_id,
                                                    shortlisted_on__gte=week_5_start,
                                                    shortlisted_on__lte=week_4_start).count()
    stats = {'views': [views1, views2, views3, views4, views5],
             'shortlists': [shortlist1, shortlist2, shortlist3, shortlist4, shortlist5],
             'appointments': [10, 25, 15, 10, 8],
             'offers': [8, 6, 16, 18, 8]
             }
    return render(request, 'statistics/graphial_stats.html', {'user_properties': user_properties,
                                                              'stats': json.dumps(stats)})
