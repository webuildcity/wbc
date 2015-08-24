# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20150724_1321'),
        ('events', '0023_auto_20150728_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='projects',
        ),
        migrations.AddField(
            model_name='event',
            name='projects',
            field=models.ForeignKey(related_name='projects__event', default=0, verbose_name=b'Projekt', blank=True, to='projects.Project'),
            preserve_default=False,
        ),
    ]
