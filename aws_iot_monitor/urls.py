"""urlconf for the aws_iot_monitor application"""

from django.conf.urls import url

from .views import home, monitor, monitor_update, about

urlpatterns = [
	url(r'^monitor_update/$', monitor_update, name='monitor_update'),
    url(r'^monitor/$', monitor, name='monitor'),
    url(r'^about/$', about, name='about'),
    url(r'^$', home, name='home'),
]