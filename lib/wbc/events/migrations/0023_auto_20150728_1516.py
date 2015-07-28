# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_auto_20150728_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='projects_events',
            new_name='projects',
        ),
    ]
