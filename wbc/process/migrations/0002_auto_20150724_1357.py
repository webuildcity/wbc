# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20150724_1357'),
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='entities',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='department',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='place',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='process_step',
        ),
        migrations.DeleteModel(
            name='Place',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
    ]
