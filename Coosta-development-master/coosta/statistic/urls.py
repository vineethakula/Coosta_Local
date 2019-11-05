from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^pageview/$', views.PageViewSet, name='property_list'),
    url(r'^get_page_view/([0-9]+)/$',
        views.GetPropertyPageViewCount.as_view(),
        name='property_page_view_count_view'),
    url(r'^$', views.statistics_home, name='statistics_home'),
]
