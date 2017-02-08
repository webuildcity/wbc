# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0037_auto_20170206_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproject',
            name='date_string',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_string',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
