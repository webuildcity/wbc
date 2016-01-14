# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20160113_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(help_text=b'Beschreibungstext', verbose_name=b'Beschreibung', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(help_text=b'Titel', max_length=256, verbose_name=b'Titel'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='begin',
            field=models.DateField(help_text=b'z.B. eines Verfahrens, B\xc3\xbcrgerbeiteiligung, Veranstaltung,etc.', verbose_name=b'Anfang'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='end',
            field=models.DateField(help_text=b'z.B. eines Verfahrens, B\xc3\xbcrgerbeiteiligung, Veranstaltung,etc.', null=True, verbose_name=b'Ende', blank=True),
        ),
    ]
