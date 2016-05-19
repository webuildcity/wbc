# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_projectattachment_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproject',
            name='finished',
            field=models.DateField(null=True, verbose_name=b'Festgestellt am', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='finished',
            field=models.DateField(null=True, verbose_name=b'Festgestellt am', blank=True),
        ),
    ]
