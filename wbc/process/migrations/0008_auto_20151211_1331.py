# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0007_auto_20151211_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processstep',
            old_name='participation',
            new_name='participation_type',
        ),
    ]
