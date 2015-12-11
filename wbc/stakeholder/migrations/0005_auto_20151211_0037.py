# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0004_auto_20151211_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stakeholder',
            name='created_by',
            field=models.ForeignKey(related_name='creator_stakeholder', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_stakeholder', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='stakeholderrole',
            name='created_by',
            field=models.ForeignKey(related_name='creator_stakeholderrole', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='stakeholderrole',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_stakeholderrole', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
