# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_remove_event_projects'),
        ('projects', '0006_auto_20150818_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='events',
            field=models.ManyToManyField(related_name='projects_events', verbose_name=b'Events', to='events.Event', blank=True),
        ),
    ]
