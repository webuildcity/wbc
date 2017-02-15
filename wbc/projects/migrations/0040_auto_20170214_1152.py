# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0039_auto_20170207_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproject',
            name='point_gis',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='historicalproject',
            name='polygon_gis',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='point_gis',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='polygon_gis',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, null=True, blank=True),
        ),
    ]
