# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='department',
            field=models.ForeignKey(verbose_name=b'Verantwortliche Organisation', blank=True, to='stakeholder.Stakeholder', null=True),
        ),
    ]
