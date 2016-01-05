# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stakeholder', '0003_department_polygon'),
    ]

    operations = [
        migrations.AddField(
            model_name='stakeholder',
            name='created_by',
            field=models.ForeignKey(related_name='creator_stakeholder', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_stakeholder', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='stakeholderrole',
            name='created_by',
            field=models.ForeignKey(related_name='creator_stakeholderrole', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='stakeholderrole',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_stakeholderrole', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
