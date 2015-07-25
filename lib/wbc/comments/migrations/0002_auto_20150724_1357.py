# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20150724_1321'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='place',
        ),
        migrations.AddField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(default=0, verbose_name=b'Ort', to='projects.Project'),
        ),
    ]
