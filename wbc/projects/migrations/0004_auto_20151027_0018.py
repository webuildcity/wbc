# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20150827_1951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='addressObj',
            new_name='address_obj',
        ),
    ]
