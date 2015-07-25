# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='addressObj',
            field=models.ForeignKey(default=0, verbose_name=b'Adresse', blank=True, to='projects.Address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='address',
            field=models.CharField(help_text=b'Eine genaue Adresse des Projekts', max_length=256, verbose_name=b'Adresse', blank=True),
        ),
    ]
