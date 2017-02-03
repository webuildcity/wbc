# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0009_basestep_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='basestep',
            name='wms',
            field=models.TextField(null=True, blank=True),
        ),
    ]
