# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0040_auto_20170214_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproject',
            name='date_string',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_string',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
    ]
