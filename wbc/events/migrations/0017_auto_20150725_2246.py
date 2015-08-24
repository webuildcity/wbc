# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_auto_20150725_2245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='projects',
            new_name='project',
        ),
    ]
