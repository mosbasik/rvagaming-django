# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'main_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'main', ['Person'])

        # Adding model 'Facebook'
        db.create_table(u'main_facebook', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Person'])),
        ))
        db.send_create_signal(u'main', ['Facebook'])

        # Adding model 'Steam'
        db.create_table(u'main_steam', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('is_main', self.gf('django.db.models.fields.BooleanField')()),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Person'])),
        ))
        db.send_create_signal(u'main', ['Steam'])

        # Adding model 'Hero'
        db.create_table(u'main_hero', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'main', ['Hero'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'main_person')

        # Deleting model 'Facebook'
        db.delete_table(u'main_facebook')

        # Deleting model 'Steam'
        db.delete_table(u'main_steam')

        # Deleting model 'Hero'
        db.delete_table(u'main_hero')


    models = {
        u'main.facebook': {
            'Meta': {'object_name': 'Facebook'},
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Person']"})
        },
        u'main.hero': {
            'Meta': {'object_name': 'Hero'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.person': {
            'Meta': {'object_name': 'Person'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.steam': {
            'Meta': {'object_name': 'Steam'},
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'is_main': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Person']"})
        }
    }

    complete_apps = ['main']