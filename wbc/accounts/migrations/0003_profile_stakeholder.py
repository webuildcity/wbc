# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0007_auto_20151211_0105'),
        ('accounts', '0002_account_renamed'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='stakeholder',
            field=models.OneToOneField(null=True, editable=False, to='stakeholder.Stakeholder', blank=True, help_text='\xd6ffentliches Profil'),
        ),
    ]
