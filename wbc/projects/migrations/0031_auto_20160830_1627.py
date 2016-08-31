# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0030_auto_20160605_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproject',
            name='featured',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicalproject',
            name='updownvote',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name='project',
            name='featured',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='updownvote',
            field=models.NullBooleanField(default=None),
        ),
    ]
