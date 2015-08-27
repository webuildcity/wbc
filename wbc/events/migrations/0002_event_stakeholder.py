# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='stakeholder',
            field=models.ManyToManyField(help_text=b'Lorem_ipsum_Test_Help_Text', related_name='stakeholders_event', verbose_name=b'stakeholders', to='stakeholder.Stakeholder', blank=True),
        ),
    ]
