# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20160115_0348'),
        ('notifications', '0005_auto_20151211_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='projects',
            field=models.ManyToManyField(to='projects.Project'),
        ),
    ]
