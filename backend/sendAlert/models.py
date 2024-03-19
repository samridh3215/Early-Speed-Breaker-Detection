from typing import Any
from django.db import models
import datetime
# Create your models here.
class Devices(models.Model):
    ip = models.CharField(verbose_name = "Device Ip", blank=False, max_length=16)
    connectionDate = models.DateField(datetime.date)
    connectionTime = models.TimeField(datetime.time)

