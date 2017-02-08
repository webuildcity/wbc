# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0036_auto_20170206_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproject',
            name='date_string',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='date_string',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
