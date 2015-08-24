# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('stakeholder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='test',
        ),
        migrations.AddField(
            model_name='organization',
            name='tags',
            field=models.ManyToManyField(related_name='tags_organization', verbose_name=b'Tags', to='tags.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='tags',
            field=models.ManyToManyField(related_name='tags_person', verbose_name=b'Tags', to='tags.Tag', blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='entities',
            field=models.ManyToManyField(related_name='places_organization', verbose_name=b'Einheit', to='region.Entity', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='entities',
            field=models.ManyToManyField(related_name='places_person', verbose_name=b'Einheit', to='region.Entity', blank=True),
        ),
    ]
