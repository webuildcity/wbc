# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0003_auto_20150818_2042'),
        ('projects', '0007_project_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='stakeholders',
            field=models.ManyToManyField(to='stakeholder.Stakeholder', verbose_name=b'Akteure', blank=True),
        ),
    ]
