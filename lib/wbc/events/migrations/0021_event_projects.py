# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20150724_1321'),
        ('events', '0020_remove_event_projects123'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='projects',
            field=models.ManyToManyField(related_name='projects__event', verbose_name=b'Projekt', to='projects.Project', blank=True),
        ),
    ]
