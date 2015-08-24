# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0005_auto_20150821_1550'),
        ('events', '0009_auto_20150821_1550'),
        ('projects', '0011_auto_20150821_1550'),
        ('tags', '0011_auto_20150821_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='WbcTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='Slug')),
                ('important', models.BooleanField(default=False, help_text=b'Hier kann bestimmt werden ob das Schlagwort in der \xc3\x9cberschrift angezeigt wird.', verbose_name=b'In \xc3\x9cberschrift anzeigen?')),
                ('visible', models.BooleanField(default=True, help_text=b'Ist das Tag sichtbar.', verbose_name=b'Sichtbar')),
            ],
            options={
                'verbose_name': 'Schlagwort (Tag)',
                'verbose_name_plural': 'Schlagw\xf6rter (Tags)',
            },
        ),
        migrations.RemoveField(
            model_name='tag',
            name='parentTag',
        ),
        migrations.AlterField(
            model_name='taggeditems',
            name='tag',
            field=models.ForeignKey(to='tags.WbcTag'),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
