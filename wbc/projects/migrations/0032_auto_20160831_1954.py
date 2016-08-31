# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0031_auto_20160830_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproject',
            name='updownvote',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='updownvote',
            field=models.NullBooleanField(default=False),
        ),
    ]
