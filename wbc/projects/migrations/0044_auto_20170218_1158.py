# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0043_auto_20170218_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalproject',
            name='clean_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='clean_date',
        ),
        migrations.AddField(
            model_name='historicalproject',
            name='year',
            field=models.IntegerField(max_length=4, null=True, verbose_name=b'Cleaned date field', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='year',
            field=models.IntegerField(max_length=4, null=True, verbose_name=b'Cleaned date field', blank=True),
        ),
    ]
