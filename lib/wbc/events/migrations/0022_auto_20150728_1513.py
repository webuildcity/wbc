# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0021_event_projects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='projects',
            new_name='projects_events',
        ),
    ]
