# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Ort.polygontype'
        db.alter_column(u'projects_ort', 'polygontype', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'Ort.polygontype'
        db.alter_column(u'projects_ort', 'polygontype', self.gf('django.db.models.fields.TextField')(default=''))

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
            'Meta': {'ordering': "('bezeichner',)", 'object_name': 'Ort'},
            'adresse': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'beschreibung': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'bezeichner': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'bezirke': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'orte'", 'symmetrical': 'False', 'to': u"orm['projects.Bezirk']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lon': ('django.db.models.fields.FloatField', [], {}),
            'polygon': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'polygontype': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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