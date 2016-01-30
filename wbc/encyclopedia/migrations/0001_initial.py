# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EncyclopediaEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('title', models.CharField(max_length=256, verbose_name=b'Titel')),
                ('gist', models.TextField(max_length=1024, verbose_name=b'Zusammenfassung')),
                ('body_text', models.TextField(verbose_name=b'Volltext')),
                ('order', models.IntegerField(help_text=b'Nummer in der Reihenfolge', verbose_name=b'Reihenfolge')),
                ('parent_entry', models.ForeignKey(related_name='sub_entries', verbose_name=b'\xc3\xbcbergeordneter Eintrag', blank=True, to='encyclopedia.EncyclopediaEntry', null=True)),
            ],
            options={
                'ordering': ('title', 'order'),
                'verbose_name': 'Lexikoneintrag',
                'verbose_name_plural': 'Lexikoneintr\xe4ge',
            },
        ),
    ]
