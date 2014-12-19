# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_worldborder_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worldborder',
            name='slug',
        ),
        migrations.AlterField(
            model_name='worldborder',
            name='mpoly',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(default=b'SRID=3857;POINT(0.0 0.0)', srid=4326),
            preserve_default=True,
        ),
    ]
