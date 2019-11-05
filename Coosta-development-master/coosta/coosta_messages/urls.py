from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^owner/$', views.contact_owner, name='contact_owner'),
    url(r'^message_box/$', views.message_box, name='message_box'),
    url(r'^message_box/(?P<sender_id>\d+)/$', views.message_box, name='message_detail'),
]