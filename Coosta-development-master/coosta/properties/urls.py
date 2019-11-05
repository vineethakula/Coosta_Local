from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^list/$', views.property_list, name='property_list'),
    url(r'^preview/(?P<property_id>[\w\-]+)/$', views.property_detail_page, name='property_detail_page'),
    url(r'^temp_preview/(?P<property_id>[\w\-]+)/$', views.property_preview_page, name='property_preview_page'),
    # url(r'^preview_old/(?P<property_id>[\w\-]+)/$', views.property_detail_page_old, name='property_detail_page_old'),
    # url(r'^recommended_properties/$', views.RecommendedPropertyViewSet.as_view({'get':'retrieve'})),
    url(r'^my_shortlisted_property/$', views.my_shortlisted_property, name='my_shortlisted_property'),
    url(r'^my_property/$', views.my_property, name='my_property'),
    url(r'^my_property/edit/(?P<property_id>[\w\-]+)/$', views.my_property, name='my_property_edit'),
    url(r'^add/property/$', views.add_property, name='add_property'),
    #url(r'^edit/property/(?P<property_id>[\w\-]+)/$', views.edit_property, name='edit_property'),
]
