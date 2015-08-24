# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0008_auto_20150509_1557'),
        ('events', '0003_auto_20150818_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='gallery',
            field=models.OneToOneField(null=True, blank=True, to='photologue.Gallery'),
        ),
    ]
