# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150724_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='addressObj',
            field=models.ForeignKey(verbose_name=b'Adresse', blank=True, to='projects.Address', null=True),
        ),
    ]
