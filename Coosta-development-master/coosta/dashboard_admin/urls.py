from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard_admin, name='dashboard_admin'),
    url(r'^(\w+)/$', views.dashboard_admin, name='dashboard_values'),
]