# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20151211_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='created_by',
            field=models.ForeignKey(related_name='creator_newsletter', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_newsletter', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='created_by',
            field=models.ForeignKey(related_name='creator_subscriber', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_subscriber', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='validation',
            name='created_by',
            field=models.ForeignKey(related_name='creator_validation', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='validation',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_validation', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
