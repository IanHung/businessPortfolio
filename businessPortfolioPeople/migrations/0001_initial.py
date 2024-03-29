# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'businessPortfolioPeople_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('briefBio', self.gf('django.db.models.fields.TextField')()),
            ('webaddress', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'businessPortfolioPeople', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'businessPortfolioPeople_person')


    models = {
        u'businessPortfolioPeople.person': {
            'Meta': {'object_name': 'Person'},
            'briefBio': ('django.db.models.fields.TextField', [], {}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'webaddress': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['businessPortfolioPeople']