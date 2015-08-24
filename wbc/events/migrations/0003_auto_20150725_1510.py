# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0003_auto_20150723_1802'),
        ('process', '0002_auto_20150724_1357'),
        ('projects', '0003_auto_20150724_1321'),
        ('region', '0001_initial'),
        ('tags', '0002_auto_20150722_1826'),
        ('events', '0002_auto_20150723_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
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
                ('office', models.TextField(verbose_name=b'Auslegungsstelle', blank=True)),
                ('office_hours', models.TextField(verbose_name=b'\xc3\x96ffnungszeiten der Auslegungsstelle', blank=True)),
                ('department', models.ForeignKey(verbose_name=b'Verantwortliche Beh\xc3\xb6rde', to='stakeholder.Stakeholder')),
                ('entities', models.ManyToManyField(related_name='places_publication', verbose_name=b'Einheit', to='region.Entity', blank=True)),
                ('process_step', models.ForeignKey(related_name='publications', verbose_name=b'Verfahrensschritt', to='process.ProcessStep')),
                ('project', models.ManyToManyField(related_name='projects__publication', verbose_name=b'Ort', to='projects.Project')),
                ('stakeholder', models.ManyToManyField(help_text=b'Lorem_ipsum_Test_Help_Text', related_name='stakeholders_publication', verbose_name=b'Stakeholder (Creator)', to='stakeholder.Stakeholder', blank=True)),
                ('tags', models.ManyToManyField(related_name='tags_publication', verbose_name=b'Tags', to='tags.Tag', blank=True)),
            ],
            options={
                'ordering': ('-end',),
                'verbose_name': 'Ver\xf6ffentlichung',
                'verbose_name_plural': 'Ver\xf6ffentlichungen',
            },
        ),
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name': 'Ereignis', 'verbose_name_plural': 'Ereignisse'},
        ),
        migrations.RenameField(
            model_name='media',
            old_name='type',
            new_name='mediatype',
        ),
        migrations.AddField(
            model_name='date',
            name='project',
            field=models.ManyToManyField(related_name='projects__date', verbose_name=b'Ort', to='projects.Project'),
        ),
        migrations.AddField(
            model_name='media',
            name='project',
            field=models.ManyToManyField(related_name='projects__media', verbose_name=b'Ort', to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='date',
            name='stakeholder',
            field=models.ManyToManyField(help_text=b'Lorem_ipsum_Test_Help_Text', related_name='stakeholders_date', verbose_name=b'Stakeholder (Creator)', to='stakeholder.Stakeholder', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='stakeholder',
            field=models.ManyToManyField(help_text=b'Lorem_ipsum_Test_Help_Text', related_name='stakeholders_media', verbose_name=b'Stakeholder (Creator)', to='stakeholder.Stakeholder', blank=True),
        ),
    ]
