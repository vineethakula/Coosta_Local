from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .routers import router
from properties import views

admin.site.site_title = 'Coosta'
admin.site.site_header = 'Coosta'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^$', views.home_page, name='home_page'),
    url(r'^user/', include('coosta_users.urls')),
    url(r'^property/', include('properties.urls')),
    url(r'^message/', include('coosta_messages.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^admin/dashboard/', include('dashboard_admin.urls')),
    url(r'^user/login/$', auth_views.login, name='login', kwargs={'redirect_authenticated_user': True}),
    url(r'^user/logout/$', auth_views.logout, name='logout'),

    # password reset
    url(r'^user/password/reset/$', auth_views.password_reset, name="password_reset"),
    url(r'^user/password/reset/done/$', auth_views.password_reset_done, name="password_reset_done"),
    url(r'^user/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^user/password/done/$', auth_views.password_reset_complete, name="password_reset_complete"),

    url(r'^email/', include('coosta_email.urls')),
    url(r'^notification/', include('coosta_notification.urls')),

    url(r'^account/', include('coosta_users.urls')),

    url(r'^api/zillow_api/(?P<address>\w+)/(?P<city>\w+)/(?P<state>\w+)/$', views.ZillowAPIView.as_view()),
    #including offers, appointments and contracts app urls
    url(r'^offers/', include('offers.urls')),
    url(r'^appointments/', include('appointments.urls')),
    url(r'^contracts/', include('contracts.urls')),
    url(r'^escrows/', include('escrows.urls')),
    url(r'^statistic/', include('statistic.urls')),
    url(r'^about_us/$', TemplateView.as_view(template_name="spa/about_us.html"), name='about_us'),
    url(r'^terms-conditions/$', TemplateView.as_view(template_name="spa/terms_condition.html"), name='terms_conditions'),
    url(r'^privacy_policy/$', TemplateView.as_view(template_name="spa/privacy_policy.html"), name='privacy_policy'),
    url(r'^how-it-works/$', TemplateView.as_view(template_name="spa/how_it_works.html"), name='how_it_works'),
    url(r'^help-faq/$', TemplateView.as_view(template_name="spa/help-faq.html"), name='help-faq'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls)),]
