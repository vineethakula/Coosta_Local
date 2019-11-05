from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^account_settings/$', views.account_settings, name='account_settings'),
    url(r'^profile_settings/$', views.profile_settings, name='profile_settings'),
    url(r'^register/$',
        views.RegistrationView.as_view(),
        name='registration_register'),
    url(r'^', include('registration.backends.hmac.urls')),
]
