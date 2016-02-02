# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0001_initial'),
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0002_subscriber_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='stakeholder',
            field=models.OneToOneField(null=True, editable=False, to='stakeholder.Stakeholder', blank=True, help_text='\xd6ffentliches Profil'),
        ),
        migrations.AddField(
            model_name='profile',
            name='subscriber',
            field=models.OneToOneField(null=True, blank=True, to='notifications.Subscriber'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
