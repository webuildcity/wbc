# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_bufferarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='bufferarea',
            name='gml_id',
            field=models.CharField(help_text=b'gml id', max_length=64, verbose_name=b'gml id', blank=True),
        ),
    ]
