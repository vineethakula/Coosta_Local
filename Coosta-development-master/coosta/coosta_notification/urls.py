from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^notification/$', views.NotificationViewSet, name='notification'),
    url(r'^notification_type/$', views.NotificationTypeViewSet,
        name='notificationtype'),
    url(r'^$', TemplateView.as_view(template_name="notifications/notifications.html"), name='notifications'),
]
