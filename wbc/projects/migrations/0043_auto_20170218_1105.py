# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0042_auto_20170217_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproject',
            name='clean_date',
            field=models.DateField(null=True, verbose_name=b'Cleaned date field', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='clean_date',
            field=models.DateField(null=True, verbose_name=b'Cleaned date field', blank=True),
        ),
    ]
