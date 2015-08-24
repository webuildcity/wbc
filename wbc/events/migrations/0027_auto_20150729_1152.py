# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0026_auto_20150728_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='modelType',
            field=models.CharField(default=b'date', max_length=20, editable=False),
        ),
        migrations.AddField(
            model_name='media',
            name='modelType',
            field=models.CharField(default=b'media', max_length=20, editable=False),
        ),
        migrations.AddField(
            model_name='publication',
            name='modelType',
            field=models.CharField(default=b'pub', max_length=20, editable=False),
        ),
    ]
