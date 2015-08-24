# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0005_auto_20150814_1018'),
        ('projects', '0003_project_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(related_name='tags_project', verbose_name=b'Tags', to='tags.Tag', blank=True),
        ),
    ]
