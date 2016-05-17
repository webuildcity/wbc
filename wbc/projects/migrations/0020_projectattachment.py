# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectAttachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('name', models.CharField(help_text=b'Name', max_length=64, null=True, verbose_name=b'Name', blank=True)),
                ('attachment', models.FileField(upload_to=b'project_attachments')),
                ('project', models.ForeignKey(verbose_name=b'Projekt', to='projects.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
