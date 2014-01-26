from django.db import models


class Metric(models.Model):
    metric_type = models.CharField(max_length=200)
    identifier = models.CharField(max_length=200)

    def __unicode__(self):
        return 'Type: %s, Identifier: %s' % (
            self.metric_type, self.identifier)


class Event(models.Model):
    metric = models.ForeignKey(Metric)
    occurred_at = models.DateTimeField()
    value = models.FloatField()

    def __unicode__(self):
        return 'Metric: %s, Occurred At: %s, Value: %s\n' % (
            self.metric.identifier, self.occurred_at, self.value)
