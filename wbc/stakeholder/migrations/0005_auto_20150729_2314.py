# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0004_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='StakeholderRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('role', models.CharField(help_text=b'Art der Rolle', max_length=64, verbose_name=b'Rolle')),
                ('slug', models.SlugField(unique=True, editable=False)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='organization',
            name='stakeholder_ptr',
        ),
        migrations.RemoveField(
            model_name='person',
            name='organizations',
        ),
        migrations.RemoveField(
            model_name='person',
            name='stakeholder_ptr',
        ),
        migrations.AlterModelOptions(
            name='stakeholder',
            options={'verbose_name': 'Akteur', 'verbose_name_plural': 'Akteure'},
        ),
        migrations.RemoveField(
            model_name='department',
            name='name',
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='name',
            field=models.CharField(default=1, help_text=b'Name des Akteurs', max_length=64, verbose_name=b'Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='slug',
            field=models.SlugField(default=1, unique=True, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='address',
            field=models.CharField(help_text=b'Eine genaue Adresse des Akteur', max_length=256, verbose_name=b'Adresse', blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='entities',
            field=models.ManyToManyField(related_name='places_stakeholder', verbose_name=b'Region', to='region.Entity', blank=True),
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='roles',
            field=models.ManyToManyField(related_name='roles_stakeholder', verbose_name=b'Rollen', to='stakeholder.StakeholderRole', blank=True),
        ),
    ]
