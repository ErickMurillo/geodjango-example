from django.contrib.gis import admin
from .models import *

# Register your models here.
admin.site.register(WorldBorder, admin.OSMGeoAdmin)
