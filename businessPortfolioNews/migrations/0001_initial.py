# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewsArticle'
        db.create_table(u'businessPortfolioNews_newsarticle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pubdate', self.gf('django.db.models.fields.DateTimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'businessPortfolioNews', ['NewsArticle'])


    def backwards(self, orm):
        # Deleting model 'NewsArticle'
        db.delete_table(u'businessPortfolioNews_newsarticle')


    models = {
        u'businessPortfolioNews.newsarticle': {
            'Meta': {'object_name': 'NewsArticle'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'pubdate': ('django.db.models.fields.DateTimeField', [], {}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['businessPortfolioNews']