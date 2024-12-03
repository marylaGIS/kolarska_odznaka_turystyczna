from django.contrib.gis.db import models
from django.conf import settings


class Place(models.Model):
    voivodeship = models.CharField(max_length=30)
    localization = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    link1 = models.CharField(max_length=255, blank=True, null=True)
    link2 = models.CharField(max_length=255, blank=True, null=True)
    geom = models.PointField(srid=4326)


class Tourist(models.Model):
    home = models.CharField(max_length=100, blank=True, null=True)
    geom = models.PointField(srid=4326, blank=True, null=True)
    public = models.BooleanField(default=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    places = models.ManyToManyField('Place', through='TouristsPlaces')


class TouristsPlaces(models.Model):
    tourist = models.ForeignKey('Tourist', on_delete=models.CASCADE)
    place = models.ForeignKey('Place', on_delete=models.CASCADE)
    visit_date = models.DateField()

