# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='begin',
            field=models.DateField(verbose_name=b'Anfang Timeline'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='process_step',
            field=models.ForeignKey(verbose_name=b'Verfahrensschritt', to='process.ProcessStep'),
        ),
    ]
