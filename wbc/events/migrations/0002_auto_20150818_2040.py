# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_squashed_0028_auto_20150818_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='projects',
            field=models.ForeignKey(related_name='projects__event', verbose_name=b'Projekt', blank=True, to='projects.Project'),
        ),
    ]
