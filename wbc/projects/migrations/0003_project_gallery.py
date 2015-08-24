# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0008_auto_20150509_1557'),
        ('projects', '0002_auto_20150729_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='gallery',
            field=models.OneToOneField(related_name='gallery', null=True, blank=True, to='photologue.Gallery'),
        ),
    ]
