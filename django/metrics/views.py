from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from models import *


def index(request):
    metrics = Metric.objects.all()
    template = loader.get_template('metrics/index.html')
    context = RequestContext(request, {
            'metric_list': metrics
        })
    return HttpResponse(template.render(context))


def metric_detail(request, metric_id):
    return HttpResponse('The detail page for metric %s' % metric_id)


def event_detail(request, event_id):
    return HttpResponse('The event detail page for event %s' % event_id)
