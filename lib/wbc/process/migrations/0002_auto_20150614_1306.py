# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('content_type', models.ForeignKey(related_name='widget_get_contenttype', editable=False, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='processstep',
            name='participation',
            field=models.CharField(max_length=256, verbose_name=b'participation', blank=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=b'Emailadresse von der Verwaltung', blank=True),
        ),
        migrations.AddField(
            model_name='participation',
            name='publication',
            field=models.ForeignKey(related_name='widgets', editable=False, to='process.Publication'),
        ),
    ]
