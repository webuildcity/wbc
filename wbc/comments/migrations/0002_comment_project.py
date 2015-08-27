# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(verbose_name=b'Ort', to='projects.Project'),
        ),
    ]
