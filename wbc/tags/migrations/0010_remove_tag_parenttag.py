# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0009_auto_20150821_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='parentTag',
        ),
    ]
