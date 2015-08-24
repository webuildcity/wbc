# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0005_auto_20150729_2314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stakeholderrole',
            options={'verbose_name': 'Rolle', 'verbose_name_plural': 'Rollen'},
        ),
    ]
