from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^openhousersvp_for_seller', views.openhousersvp_for_seller,
        name='openhousersvp_for_seller'),
]
