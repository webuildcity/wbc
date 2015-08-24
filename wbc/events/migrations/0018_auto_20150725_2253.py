# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_auto_20150725_2246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='project',
            new_name='projects',
        ),
    ]
