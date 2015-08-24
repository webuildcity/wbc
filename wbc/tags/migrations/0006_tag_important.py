# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0005_auto_20150814_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='important',
            field=models.BooleanField(default=False, help_text=b'Hier kann bestimmt werden ob das Schlagwort in der \xc3\x9cberschrift angezeigt wird.', verbose_name=b'In \xc3\x9cberschrift anzeigen?'),
        ),
    ]
