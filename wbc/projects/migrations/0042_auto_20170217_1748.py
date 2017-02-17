# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0041_auto_20170214_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproject',
            name='quarter',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='quarter',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
    ]
