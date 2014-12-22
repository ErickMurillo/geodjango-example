
from django.contrib.gis.db import models

# Create your models here.

class Municipios(models.Model):
    area = models.FloatField()
    perimeter = models.FloatField()
    limites_field = models.FloatField()
    limites_id = models.FloatField()
    munic_id = models.IntegerField()
    depto_id = models.IntegerField()
    depto = models.CharField(max_length=35)
    municipio = models.CharField(max_length=35)
    croquis = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

