# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table(u'businessPortfolioCompanies_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('abstract', self.gf('django.db.models.fields.TextField')()),
            ('webaddress', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('dateFounded', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'businessPortfolioCompanies', ['Company'])


    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table(u'businessPortfolioCompanies_company')


    models = {
        u'businessPortfolioCompanies.company': {
            'Meta': {'object_name': 'Company'},
            'abstract': ('django.db.models.fields.TextField', [], {}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'dateFounded': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'webaddress': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['businessPortfolioCompanies']