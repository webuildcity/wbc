# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0006_auto_20151211_0105'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=256, verbose_name=b'Name')),
                ('description', models.TextField(verbose_name=b'Beschreibung')),
                ('participation', models.BooleanField(default=False)),
                ('icon', models.CharField(max_length=256, verbose_name=b'Icon')),
            ],
            options={
                'verbose_name': 'Partizipationsform',
                'verbose_name_plural': 'Partizipationsformen',
            },
        ),
        migrations.RemoveField(
            model_name='processstep',
            name='participation',
        ),
        migrations.AddField(
            model_name='processstep',
            name='participation',
            field=models.ForeignKey(related_name='process_steps', verbose_name=b'Partizipation', to='process.ParticipationType'),
        ),
    ]
