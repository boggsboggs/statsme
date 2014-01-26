from django.contrib import admin
from metrics.models import Metric, Event

admin.site.register(Metric)
admin.site.register(Event)
