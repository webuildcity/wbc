# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0003_auto_20150723_1802'),
        ('projects', '0003_auto_20150724_1321'),
        ('region', '0001_initial'),
        ('tags', '0002_auto_20150722_1826'),
        ('events', '0003_auto_20150725_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('title', models.CharField(help_text=b'Der Titel eines Events', max_length=256, verbose_name=b'Titel')),
                ('description', models.TextField(help_text=b'Beschreibungstext eines Events', verbose_name=b'Beschreibung', blank=True)),
                ('link', models.URLField(blank=True)),
                ('active', models.BooleanField()),
                ('begin', models.DateField(verbose_name=b'Beginn')),
                ('end', models.DateField(verbose_name=b'Ende der Auslegungszeit', blank=True)),
                ('entities', models.ManyToManyField(related_name='places_event', verbose_name=b'Einheit', to='region.Entity', blank=True)),
                ('project', models.ManyToManyField(related_name='projects__event', verbose_name=b'Projekt', to='projects.Project')),
                ('stakeholder', models.ManyToManyField(help_text=b'Lorem_ipsum_Test_Help_Text', related_name='stakeholders_event', verbose_name=b'Stakeholder (Creator)', to='stakeholder.Stakeholder', blank=True)),
                ('tags', models.ManyToManyField(related_name='tags_event', verbose_name=b'Tags', to='tags.Tag', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name': 'Medienbeitrag', 'verbose_name_plural': 'Medienbeitr\xe4ge'},
        ),
        migrations.RemoveField(
            model_name='date',
            name='active',
        ),
        migrations.RemoveField(
            model_name='date',
            name='begin',
        ),
        migrations.RemoveField(
            model_name='date',
            name='created',
        ),
        migrations.RemoveField(
            model_name='date',
            name='description',
        ),
        migrations.RemoveField(
            model_name='date',
            name='end',
        ),
        migrations.RemoveField(
            model_name='date',
            name='entities',
        ),
        migrations.RemoveField(
            model_name='date',
            name='id',
        ),
        migrations.RemoveField(
            model_name='date',
            name='link',
        ),
        migrations.RemoveField(
            model_name='date',
            name='project',
        ),
        migrations.RemoveField(
            model_name='date',
            name='stakeholder',
        ),
        migrations.RemoveField(
            model_name='date',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='date',
            name='title',
        ),
        migrations.RemoveField(
            model_name='date',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='media',
            name='active',
        ),
        migrations.RemoveField(
            model_name='media',
            name='begin',
        ),
        migrations.RemoveField(
            model_name='media',
            name='created',
        ),
        migrations.RemoveField(
            model_name='media',
            name='description',
        ),
        migrations.RemoveField(
            model_name='media',
            name='end',
        ),
        migrations.RemoveField(
            model_name='media',
            name='entities',
        ),
        migrations.RemoveField(
            model_name='media',
            name='id',
        ),
        migrations.RemoveField(
            model_name='media',
            name='link',
        ),
        migrations.RemoveField(
            model_name='media',
            name='project',
        ),
        migrations.RemoveField(
            model_name='media',
            name='stakeholder',
        ),
        migrations.RemoveField(
            model_name='media',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='media',
            name='title',
        ),
        migrations.RemoveField(
            model_name='media',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='active',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='begin',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='created',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='description',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='end',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='entities',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='id',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='link',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='project',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='stakeholder',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='title',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='updated',
        ),
        migrations.AddField(
            model_name='date',
            name='event_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=0, serialize=False, to='events.Event'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='event_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=0, serialize=False, to='events.Event'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publication',
            name='event_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=0, serialize=False, to='events.Event'),
            preserve_default=False,
        ),
    ]
