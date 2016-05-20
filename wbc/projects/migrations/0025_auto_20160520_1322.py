# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0024_auto_20160520_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bufferarea',
            name='gml_id',
            field=models.CharField(help_text=b'gml id', max_length=128, verbose_name=b'gml id', blank=True),
        ),
    ]
