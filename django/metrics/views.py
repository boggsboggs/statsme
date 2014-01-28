from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View

from django.core.urlresolvers import reverse_lazy
from django.utils import timezone

import logging

from models import *


class MetricListContextView(object):
    def get_context_data(self, **kwargs):
        context = super(MetricListContextView, self).get_context_data(**kwargs)
        context['metric_list'] = Metric.objects.all()
        return context


# Metric CRUD
class MetricCreate(CreateView):
    model = Metric
    fields = ['identifier']


class MetricDetail(MetricListContextView, DetailView):
    model = Metric

    def get_context_data(self, **kwargs):
        context = super(MetricDetail, self).get_context_data(**kwargs)
        context['metric_id'] = self.object.id
        return context


class MetricUpdate(UpdateView):
    model = Metric
    fields = ['identifier']


class MetricDelete(DeleteView):
    model = Metric
    success_url = reverse_lazy('metric-list')


# Event CRUD
class EventCreate(View):
    def post(self, *args, **kwargs):
        metric = get_object_or_404(Metric, pk=self.kwargs['metric_pk'])
        value = self.request.POST['value']
        event = Event(metric=metric, occurred_at=timezone.now(), value=value)
        event.save()
        redirect_url = event.metric.get_absolute_url()
        logging.info(redirect_url)
        return HttpResponseRedirect(redirect_url)


class EventDetail(View):
    pass


class EventUpdate(View):
    pass


class EventDelete(View):
    pass
