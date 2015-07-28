# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0025_auto_20150728_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='subject',
        ),
        migrations.AlterField(
            model_name='media',
            name='provenance',
            field=models.CharField(help_text=b'Welche Zweifel oder Probleme gibt es mit dem Dokument?', max_length=128, verbose_name=b'Echtheit des Dokuments', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='provenanceactive',
            field=models.BooleanField(verbose_name=b'Echtheit des Dokuments gepr\xc3\xbcft'),
        ),
    ]
