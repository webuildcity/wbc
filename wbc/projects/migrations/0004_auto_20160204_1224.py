# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20160130_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproject',
            name='polygon_alter',
            field=models.TextField(help_text=b'Ausgleichsfl\xc3\xa4che nach Bundesumweltgesetz', null=True, verbose_name=b'Ausgleichsfl\xc3\xa4che', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='polygon_alter',
            field=models.TextField(help_text=b'Ausgleichsfl\xc3\xa4che nach Bundesumweltgesetz', null=True, verbose_name=b'Ausgleichsfl\xc3\xa4che', blank=True),
        ),
    ]
