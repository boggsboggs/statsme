from django.views.generic.detail import DetailView
from django.views.generic import ListView

from django.conf.urls import patterns, url

from metrics.models import *
from metrics.views import *

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(model=Metric),
        name='metric_list'),

    # Metric CRUD
    url(r'metric/create/?',
        MetricCreate.as_view(template_name='metric_list.html'),
        name='metric_create'),

    url(r'^metric/(?P<pk>\d+)/?$',
        MetricDetail.as_view(),
        name='metric_detail'),

    url(r'^metric/(?P<pk>\d+)/update/?$',
        MetricCreate.as_view(template_name='metric_list.html'),
        name='metric_update'),

    url(r'^metric/(?P<pk>\d+)/delete/?$',
        MetricDelete.as_view(template_name='metric_list.html'),
        name='metric_delete'),

    # Event CRUD
    url(r'^metric/(?P<metric_pk>\d+)/create/?$',
        EventCreate.as_view(),
        name='event_create'),

    url(r'^metric/(?P<metric_pk>\d+)/event_(?P<pk>\d+)/?$',
        DetailView.as_view(model=Event),
        name='event_detail'),
)
