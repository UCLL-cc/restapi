from datetime import datetime

from django.db import models


class Day(models.Model):
    date = models.DateField()


class Trigger(models.Model):
    time = models.TimeField()
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='triggers')

    def date_hour(self):
        return datetime.datetime.fromtimestamp(self.time).strftime("%H")
