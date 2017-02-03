# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0008_basestep_fulltext'),
    ]

    operations = [
        migrations.AddField(
            model_name='basestep',
            name='audio',
            field=models.TextField(null=True, blank=True),
        ),
    ]
