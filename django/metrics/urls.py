from django.conf.urls import patterns, url

from metrics import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^metric/(?P<metric_id>\d+)/?$', views.metric_detail, name='metric_detail'),
    url(r'^event/(?P<event_id>\d+)/?$', views.event_detail, name='event_detail'),
)
