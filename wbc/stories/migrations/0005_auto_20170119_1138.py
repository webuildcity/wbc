# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20170109_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basestep',
            old_name='lon',
            new_name='lng',
        ),
    ]
