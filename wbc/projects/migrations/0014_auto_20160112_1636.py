# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20160112_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='cover_photo',
            field=models.ForeignKey(related_name='cover', blank=True, to='projects.Photo', null=True),
        ),
    ]
