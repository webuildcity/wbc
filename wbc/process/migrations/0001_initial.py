# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=256, verbose_name=b'Name')),
                ('description', models.TextField(verbose_name=b'Beschreibung', blank=True)),
                ('participation', models.BooleanField(default=False, verbose_name=b'Partizipation m\xc3\xb6glich')),
                ('icon', models.CharField(max_length=256, verbose_name=b'Icon')),
                ('encyclopedia_entry', models.ForeignKey(verbose_name=b'Lexikoneintrag', blank=True, to='encyclopedia.EncyclopediaEntry', null=True)),
            ],
            options={
                'verbose_name': 'Partizipationsform',
                'verbose_name_plural': 'Partizipationsformen',
            },
        ),
        migrations.CreateModel(
            name='ProcessStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=256, verbose_name=b'Name')),
                ('description', models.TextField(verbose_name=b'Beschreibung')),
                ('icon', models.CharField(max_length=256, verbose_name=b'Icon auf der Karte')),
                ('hover_icon', models.CharField(max_length=256, verbose_name=b'Icon auf der Karte bei Hovereffekt')),
                ('order', models.IntegerField(help_text=b'Nummer in der Reihenfolge', verbose_name=b'Reihenfolge')),
                ('encyclopedia_entry', models.ForeignKey(verbose_name=b'Lexikoneintrag', blank=True, to='encyclopedia.EncyclopediaEntry', null=True)),
                ('parent_step', models.ForeignKey(related_name='sub_process_steps', verbose_name=b'\xc3\xbcbergeordneter Verfahrensschritt', blank=True, to='process.ProcessStep', null=True)),
                ('participation_type', models.ForeignKey(related_name='process_steps', verbose_name=b'Partizipation', to='process.ParticipationType')),
            ],
            options={
                'ordering': ('process_type', 'order'),
                'verbose_name': 'Verfahrensschritt',
                'verbose_name_plural': 'Verfahrensschritte',
            },
        ),
        migrations.CreateModel(
            name='ProcessType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=256, verbose_name=b'Name')),
                ('description', models.TextField(verbose_name=b'Beschreibung')),
                ('encyclopedia_entry', models.ForeignKey(verbose_name=b'Lexikoneintrag', blank=True, to='encyclopedia.EncyclopediaEntry', null=True)),
            ],
            options={
                'verbose_name': 'Verfahren',
                'verbose_name_plural': 'Verfahren',
            },
        ),
        migrations.AddField(
            model_name='processstep',
            name='process_type',
            field=models.ForeignKey(related_name='process_steps', verbose_name=b'Verfahren', to='process.ProcessType'),
        ),
    ]
