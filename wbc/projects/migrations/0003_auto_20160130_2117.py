# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0001_initial'),
        ('projects', '0002_project_stakeholders'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '0001_initial'),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags',
            field=taggit.managers.TaggableManager(to='tags.WbcTag', through='tags.TaggedItems', blank=True, help_text='A comma-separated list of tags.', verbose_name=b'Schlagworte'),
        ),
        migrations.AddField(
            model_name='historicalproject',
            name='address_obj',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='projects.Address', null=True),
        ),
        migrations.AddField(
            model_name='historicalproject',
            name='album',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='images.Album', null=True),
        ),
        migrations.AddField(
            model_name='historicalproject',
            name='history_user',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='historicalproject',
            name='owner',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(verbose_name=b'Stadt', to='region.Muncipality'),
        ),
        migrations.AddField(
            model_name='address',
            name='entities',
            field=models.ManyToManyField(related_name='adress_places', verbose_name=b'Einheit', to='region.Entity', blank=True),
        ),
    ]
