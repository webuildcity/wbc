# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_event_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='projects',
            field=models.ManyToManyField(related_name='projects__event', verbose_name=b'Projekt', to='projects.Project', blank=True),
        ),
    ]
