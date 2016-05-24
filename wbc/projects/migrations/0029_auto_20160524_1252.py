# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0028_auto_20160524_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproject',
            name='isFinished',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='isFinished',
            field=models.NullBooleanField(default=True),
        ),
    ]
