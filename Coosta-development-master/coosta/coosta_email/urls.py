from django.conf.urls import url

from .views import (PasswordResetView, PasswordResetConfirmView, SendEmailView)

urlpatterns = [
    # URLs that do not require a session or valid token
    url(r'^password/reset/$', PasswordResetView.as_view(),
        name='rest_password_reset'),
    url(r'^password/reset/confirm/$', PasswordResetConfirmView.as_view(),
        name='rest_password_reset_confirm'),
    url(r'^send-email/$', SendEmailView.as_view(), name='send_email'),
]
