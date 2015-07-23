# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0001_initial'),
        ('tags', '0002_auto_20150722_1826'),
        ('stakeholder', '0002_auto_20150722_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stakeholder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('address', models.CharField(help_text=b'Eine genaue Adresse des Stakeholders', max_length=256, verbose_name=b'Adresse', blank=True)),
                ('description', models.TextField(help_text=b'Beschreibung des Stakeholders', verbose_name=b'Beschreibung', blank=True)),
                ('active', models.BooleanField()),
                ('link', models.URLField(blank=True)),
                ('entities', models.ManyToManyField(related_name='places_stakeholder', verbose_name=b'Einheit', to='region.Entity', blank=True)),
                ('tags', models.ManyToManyField(related_name='tags_stakeholder', verbose_name=b'Tags', to='tags.Tag', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='organization',
            name='active',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='address',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='created',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='description',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='entities',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='id',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='link',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='person',
            name='active',
        ),
        migrations.RemoveField(
            model_name='person',
            name='address',
        ),
        migrations.RemoveField(
            model_name='person',
            name='created',
        ),
        migrations.RemoveField(
            model_name='person',
            name='description',
        ),
        migrations.RemoveField(
            model_name='person',
            name='entities',
        ),
        migrations.RemoveField(
            model_name='person',
            name='id',
        ),
        migrations.RemoveField(
            model_name='person',
            name='link',
        ),
        migrations.RemoveField(
            model_name='person',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='person',
            name='updated',
        ),
        migrations.AddField(
            model_name='organization',
            name='stakeholder_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='stakeholder.Stakeholder'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='stakeholder_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='stakeholder.Stakeholder'),
            preserve_default=False,
        ),
    ]
