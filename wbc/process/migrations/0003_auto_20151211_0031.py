# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('process', '0002_processstep_participation'),
    ]

    operations = [
        migrations.AddField(
            model_name='processstep',
            name='created_by',
            field=models.ForeignKey(related_name='creator_processstep', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='processstep',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_processstep', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='processtype',
            name='created_by',
            field=models.ForeignKey(related_name='creator_processtype', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='processtype',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_processtype', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
