# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_auto_20160520_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproject',
            name='isFinished',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='isFinished',
            field=models.BooleanField(default=True),
        ),
    ]
