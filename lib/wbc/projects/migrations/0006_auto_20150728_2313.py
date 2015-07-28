# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='tags',
        ),
        migrations.AlterField(
            model_name='project',
            name='address',
            field=models.CharField(help_text=b'Altes, statisches Adress-Feld', max_length=256, verbose_name=b'Adresse (Statisch)', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='entities',
            field=models.ManyToManyField(related_name='project_places', verbose_name=b'Verwaltungseinheit', to='region.Entity', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(unique=True, editable=False),
        ),
    ]
