# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0045_auto_20170220_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproject',
            name='slug',
            field=models.SlugField(null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(null=True, editable=False, blank=True, unique=True),
        ),
    ]
