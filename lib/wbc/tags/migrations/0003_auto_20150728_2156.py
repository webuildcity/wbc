# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_auto_20150722_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='abbreviation',
            field=models.CharField(help_text=b'K\xc3\xbcrzel', max_length=256, verbose_name=b'Abk\xc3\xbcrzung', blank=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='parentTag',
            field=models.ForeignKey(default=0, blank=True, to='tags.Tag'),
            preserve_default=False,
        ),
    ]
