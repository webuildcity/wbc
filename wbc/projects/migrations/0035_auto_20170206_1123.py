# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0034_auto_20161205_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproject',
            name='typename',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='typename',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
