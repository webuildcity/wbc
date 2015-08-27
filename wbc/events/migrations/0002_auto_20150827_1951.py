# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0001_initial'),
        ('stakeholder', '0001_initial'),
        ('events', '0001_initial'),
        ('process', '0001_initial'),
        ('projects', '0001_initial'),
        ('photologue', '0008_auto_20150509_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='department',
            field=models.ForeignKey(verbose_name=b'Verantwortliche Beh\xc3\xb6rde', to='stakeholder.Stakeholder'),
        ),
        migrations.AddField(
            model_name='publication',
            name='process_step',
            field=models.ForeignKey(related_name='publications', verbose_name=b'Verfahrensschritt', to='process.ProcessStep'),
        ),
        migrations.AddField(
            model_name='publication',
            name='project',
            field=models.ForeignKey(verbose_name=b'Projekt', to='projects.Project'),
        ),
        migrations.AddField(
            model_name='event',
            name='entities',
            field=models.ManyToManyField(related_name='places_event', verbose_name=b'Region', to='region.Entity', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='gallery',
            field=models.OneToOneField(null=True, blank=True, to='photologue.Gallery'),
        ),
        migrations.AddField(
            model_name='event',
            name='stakeholder',
            field=models.ManyToManyField(help_text=b'Lorem_ipsum_Test_Help_Text', related_name='stakeholders_event', verbose_name=b'stakeholders', to='stakeholder.Stakeholder', blank=True),
        ),
    ]
