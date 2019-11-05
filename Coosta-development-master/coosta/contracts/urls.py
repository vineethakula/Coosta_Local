from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sign/(?P<contract_id>[\w\-]+)/$', views.sign_contract, name='sign_contract')
]