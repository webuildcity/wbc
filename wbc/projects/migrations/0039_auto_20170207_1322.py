# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0038_auto_20170207_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproject',
            name='identifier',
            field=models.CharField(help_text=b'ggf. Bezeichner des Projekts', max_length=128, null=True, verbose_name=b'Bezeichner', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='identifier',
            field=models.CharField(help_text=b'ggf. Bezeichner des Projekts', max_length=128, null=True, verbose_name=b'Bezeichner', blank=True),
        ),
    ]
