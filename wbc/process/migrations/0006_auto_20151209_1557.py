# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0005_auto_20151204_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('title', models.CharField(max_length=256, verbose_name=b'Titel')),
                ('gist', models.CharField(max_length=512, verbose_name=b'Kurztext')),
                ('body_text', models.TextField(verbose_name=b'Text')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name=b'erstellt am')),
                ('modified_at', models.DateField(auto_now=True, verbose_name=b'zuletzt ge\xc3\xa4ndert am')),
            ],
            options={
                'verbose_name': 'Artikel',
                'verbose_name_plural': 'Artikel',
            },
        ),
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=256, verbose_name=b'Name')),
            ],
            options={
                'verbose_name': 'Artikelart',
                'verbose_name_plural': 'Artikelarten',
            },
        ),
        migrations.RemoveField(
            model_name='participationform',
            name='description',
        ),
        migrations.RemoveField(
            model_name='processstep',
            name='description',
        ),
        migrations.RemoveField(
            model_name='processtype',
            name='description',
        ),
        migrations.AddField(
            model_name='article',
            name='article_type',
            field=models.ForeignKey(related_name='articles', verbose_name=b'Artikelart', to='process.ArticleType'),
        ),
        migrations.AddField(
            model_name='participationform',
            name='article',
            field=models.ForeignKey(verbose_name=b'Beschreibung', to='process.Article', null=True),
        ),
        migrations.AddField(
            model_name='processstep',
            name='article',
            field=models.ForeignKey(verbose_name=b'Beschreibung', to='process.Article', null=True),
        ),
        migrations.AddField(
            model_name='processtype',
            name='article',
            field=models.ForeignKey(verbose_name=b'Beschreibung', to='process.Article', null=True),
        ),
    ]
