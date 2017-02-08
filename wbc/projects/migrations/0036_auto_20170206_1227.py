# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0035_auto_20170206_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproject',
            name='area',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='historicalproject',
            name='length',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='area',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='length',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
