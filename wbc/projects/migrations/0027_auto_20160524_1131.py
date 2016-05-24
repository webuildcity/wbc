# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0026_auto_20160520_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproject',
            name='identifier',
            field=models.CharField(help_text=b'ggf. Bezeichner des Projekts', max_length=128, verbose_name=b'Bezeichner', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='name',
            field=models.CharField(help_text=b'Name des Projekts', max_length=128, verbose_name=b'Name'),
        ),
        migrations.AlterField(
            model_name='project',
            name='identifier',
            field=models.CharField(help_text=b'ggf. Bezeichner des Projekts', max_length=128, verbose_name=b'Bezeichner', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(help_text=b'Name des Projekts', max_length=128, verbose_name=b'Name'),
        ),
    ]
