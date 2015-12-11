# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0003_auto_20151211_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processstep',
            name='created_by',
            field=models.ForeignKey(related_name='creator_processstep', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='processstep',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_processstep', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='processtype',
            name='created_by',
            field=models.ForeignKey(related_name='creator_processtype', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='processtype',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_processtype', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
