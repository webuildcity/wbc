# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ort'
        db.create_table(u'projects_ort', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('adresse', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('beschreibung', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('lon', self.gf('django.db.models.fields.FloatField')()),
            ('bezeichner', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Ort'])

        # Adding M2M table for field bezirke on 'Ort'
        m2m_table_name = db.shorten_name(u'projects_ort_bezirke')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ort', models.ForeignKey(orm[u'projects.ort'], null=False)),
            ('bezirk', models.ForeignKey(orm[u'projects.bezirk'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ort_id', 'bezirk_id'])

        # Adding model 'Veroeffentlichung'
        db.create_table(u'projects_veroeffentlichung', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('beschreibung', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('verfahrensschritt', self.gf('django.db.models.fields.related.ForeignKey')(related_name='veroeffentlichungen', to=orm['projects.Verfahrensschritt'])),
            ('ort', self.gf('django.db.models.fields.related.ForeignKey')(related_name='veroeffentlichungen', to=orm['projects.Ort'])),
            ('beginn', self.gf('django.db.models.fields.DateField')()),
            ('ende', self.gf('django.db.models.fields.DateField')()),
            ('auslegungsstelle', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('zeiten', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('behoerde', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Behoerde'])),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Veroeffentlichung'])

        # Adding model 'Verfahrensschritt'
        db.create_table(u'projects_verfahrensschritt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('beschreibung', self.gf('django.db.models.fields.TextField')()),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('hoverIcon', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('reihenfolge', self.gf('django.db.models.fields.IntegerField')()),
            ('verfahren', self.gf('django.db.models.fields.related.ForeignKey')(related_name='verfahrensschritte', to=orm['projects.Verfahren'])),
        ))
        db.send_create_signal(u'projects', ['Verfahrensschritt'])

        # Adding model 'Verfahren'
        db.create_table(u'projects_verfahren', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('beschreibung', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'projects', ['Verfahren'])

        # Adding model 'Behoerde'
        db.create_table(u'projects_behoerde', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Behoerde'])

        # Adding model 'Bezirk'
        db.create_table(u'projects_bezirk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'projects', ['Bezirk'])


    def backwards(self, orm):
        # Deleting model 'Ort'
        db.delete_table(u'projects_ort')

        # Removing M2M table for field bezirke on 'Ort'
        db.delete_table(db.shorten_name(u'projects_ort_bezirke'))

        # Deleting model 'Veroeffentlichung'
        db.delete_table(u'projects_veroeffentlichung')

        # Deleting model 'Verfahrensschritt'
        db.delete_table(u'projects_verfahrensschritt')

        # Deleting model 'Verfahren'
        db.delete_table(u'projects_verfahren')

        # Deleting model 'Behoerde'
        db.delete_table(u'projects_behoerde')

        # Deleting model 'Bezirk'
        db.delete_table(u'projects_bezirk')


    models = {
        u'projects.behoerde': {
            'Meta': {'object_name': 'Behoerde'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'projects.bezirk': {
            'Meta': {'object_name': 'Bezirk'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'projects.ort': {
            'Meta': {'object_name': 'Ort'},
            'adresse': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'beschreibung': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'bezeichner': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'bezirke': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'orte'", 'symmetrical': 'False', 'to': u"orm['projects.Bezirk']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lon': ('django.db.models.fields.FloatField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'projects.verfahren': {
            'Meta': {'object_name': 'Verfahren'},
            'beschreibung': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'projects.verfahrensschritt': {
            'Meta': {'ordering': "('verfahren', 'reihenfolge')", 'object_name': 'Verfahrensschritt'},
            'beschreibung': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'hoverIcon': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'reihenfolge': ('django.db.models.fields.IntegerField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {}),
            'verfahren': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'verfahrensschritte'", 'to': u"orm['projects.Verfahren']"})
        },
        u'projects.veroeffentlichung': {
            'Meta': {'ordering': "('-ende',)", 'object_name': 'Veroeffentlichung'},
            'auslegungsstelle': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'beginn': ('django.db.models.fields.DateField', [], {}),
            'behoerde': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Behoerde']"}),
            'beschreibung': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'ende': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'ort': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'veroeffentlichungen'", 'to': u"orm['projects.Ort']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {}),
            'verfahrensschritt': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'veroeffentlichungen'", 'to': u"orm['projects.Verfahrensschritt']"}),
            'zeiten': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['projects']