# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='stakeholders',
            field=models.ManyToManyField(to='stakeholder.Stakeholder', verbose_name=b'Akteure', blank=True),
        ),
    ]
