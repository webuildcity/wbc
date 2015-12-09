# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0002_processstep_participation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipationForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=256, verbose_name=b'Name')),
                ('description', models.TextField(verbose_name=b'Beschreibung')),
                ('icon', models.CharField(max_length=256, verbose_name=b'Icon auf der Karte')),
                ('hover_icon', models.CharField(max_length=256, verbose_name=b'Icon auf der Karte bei Hovereffekt')),
                ('participation', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Form der B\xfcrgerbeteiligung',
                'verbose_name_plural': 'Formen der B\xfcrgerbeteiligung',
            },
        ),
        migrations.RemoveField(
            model_name='processstep',
            name='participation',
        ),
        migrations.AddField(
            model_name='processstep',
            name='parent_step',
            field=models.ForeignKey(related_name='process_steps', verbose_name=b'\xc3\x9cbergeordneter Verfahrensschritt', to='process.ProcessStep', null=True),
        ),
        migrations.AddField(
            model_name='processstep',
            name='participation_form',
            field=models.ForeignKey(related_name='process_steps', verbose_name=b'Form der B\xc3\xbcrgerbeteiligung', to='process.ParticipationForm', null=True),
        ),
    ]
