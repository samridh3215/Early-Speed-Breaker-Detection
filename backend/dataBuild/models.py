from django.db import models

# Create your models here.
class SpeedBreakerData(models.Model):
    lat = models.FloatField(verbose_name="Latitutude", max_length=9, blank=False)
    long = models.FloatField(verbose_name="Latitutude", max_length=9, blank=False)
    tally = models.IntegerField(verbose_name="Tally", blank=False)
