# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_bufferarea_gml_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bufferarea',
            name='project',
            field=models.ForeignKey(verbose_name=b'Projekt', blank=True, to='projects.Project', null=True),
        ),
        migrations.AlterField(
            model_name='bufferarea',
            name='area',
            field=models.FloatField(help_text=b'Fl\xc3\xa4che in m\xc2\xb2', null=True, verbose_name=b'Flaeche', blank=True),
        ),
    ]
