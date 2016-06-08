# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0029_auto_20160524_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproject',
            name='padId',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='padId',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
