# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20151211_0105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='date',
            options={'verbose_name': 'Veranstaltung (Event)', 'verbose_name_plural': 'Veranstaltungen (Events)'},
        ),
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name': 'Informationsbeitrag', 'verbose_name_plural': 'Informationsbeitr\xe4ge'},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ('-end',), 'verbose_name': 'Prozessschritt', 'verbose_name_plural': 'Prozesschritte'},
        ),
        migrations.RemoveField(
            model_name='publication',
            name='office',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='office_hours',
        ),
        migrations.AlterField(
            model_name='date',
            name='other',
            field=models.CharField(help_text=b'Sonstige Angaben zu dieser Veranstaltung', max_length=256, verbose_name=b'Sonstiges', blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='begin',
            field=models.DateField(verbose_name=b'Anfang des Ereignisses'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='department',
            field=models.ForeignKey(verbose_name=b'Verantwortliche Organisation', to='stakeholder.Stakeholder'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='end',
            field=models.DateField(null=True, verbose_name=b'Ende des Ereignisses', blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='link',
            field=models.URLField(help_text=b'Weiterf\xc3\xbchrender Link (optional)', verbose_name=b'Link', blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='process_step',
            field=models.ForeignKey(verbose_name=b'Prozessschritt', to='process.ProcessStep', help_text=b'z.B. Demografiewerkstatt, \xc3\x96ffentliche Auslegung, eine Wahl, etc.'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='project',
            field=models.ForeignKey(verbose_name=b'Betreffendes Projekt', to='projects.Project'),
        ),
    ]
