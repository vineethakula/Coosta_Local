from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^closing-agent/(?P<closing_agent_id>[\w\-]+)/$', views.closing_agent, name='closing_agent')
]