# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0044_auto_20170218_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproject',
            name='year',
            field=models.IntegerField(db_index=True, null=True, verbose_name=b'Cleaned date field', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='year',
            field=models.IntegerField(db_index=True, null=True, verbose_name=b'Cleaned date field', blank=True),
        ),
    ]
