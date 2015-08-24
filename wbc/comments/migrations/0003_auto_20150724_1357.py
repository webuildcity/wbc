# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20150724_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(verbose_name=b'Ort', to='projects.Project'),
        ),
    ]
