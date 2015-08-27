# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
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
