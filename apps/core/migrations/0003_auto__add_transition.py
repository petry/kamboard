# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Transition'
        db.create_table(u'core_transition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('story', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Story'])),
            ('step', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Step'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Transition'])


    def backwards(self, orm):
        # Deleting model 'Transition'
        db.delete_table(u'core_transition')


    models = {
        u'core.board': {
            'Meta': {'object_name': 'Board'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.step': {
            'Meta': {'object_name': 'Step'},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Board']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'next': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Step']"})
        },
        u'core.story': {
            'Meta': {'object_name': 'Story'},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Board']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.transition': {
            'Meta': {'object_name': 'Transition'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'step': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Step']"}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Story']"})
        }
    }

    complete_apps = ['core']