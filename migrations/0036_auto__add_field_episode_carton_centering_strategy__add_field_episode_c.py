# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Episode.carton_centering_strategy'
        db.add_column(u'deck_episode', 'carton_centering_strategy',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)

        # Adding field 'Episode.carton_background_color'
        db.add_column(u'deck_episode', 'carton_background_color',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)

        # Adding field 'Show.carton_centering_strategy'
        db.add_column(u'deck_show', 'carton_centering_strategy',
                      self.gf('django.db.models.fields.CharField')(default='stretched', max_length=20),
                      keep_default=False)

        # Adding field 'Show.carton_background_color'
        db.add_column(u'deck_show', 'carton_background_color',
                      self.gf('django.db.models.fields.CharField')(default='transparent', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Episode.carton_centering_strategy'
        db.delete_column(u'deck_episode', 'carton_centering_strategy')

        # Deleting field 'Episode.carton_background_color'
        db.delete_column(u'deck_episode', 'carton_background_color')

        # Deleting field 'Show.carton_centering_strategy'
        db.delete_column(u'deck_show', 'carton_centering_strategy')

        # Deleting field 'Show.carton_background_color'
        db.delete_column(u'deck_show', 'carton_background_color')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'deck.category': {
            'Meta': {'object_name': 'Category'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'#CCCCCC'", 'max_length': '20'}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'deck.download': {
            'Meta': {'object_name': 'Download'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['deck.Episode']"}),
            'extension': ('django.db.models.fields.CharField', [], {'default': "'.mp3'", 'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': '"L\'\\xc3\\xa9mission"', 'max_length': '30'}),
            'size': ('django.db.models.fields.CharField', [], {'default': "'10 Mo'", 'max_length': '10', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'deck.episode': {
            'Meta': {'object_name': 'Episode'},
            'carton_background_color': ('django.db.models.fields.CharField', [], {'default': "'transparent'", 'max_length': '20'}),
            'carton_centering_strategy': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'carton_content': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'carton_image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'carton_title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'livepage_bg_image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': "'10'"}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'show': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['deck.Show']"}),
            'shown': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'deck.livepage': {
            'Meta': {'object_name': 'LivePage'},
            'css': ('django.db.models.fields.TextField', [], {'default': "'/* Code CSS ici */'"}),
            'footer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'producer_image': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'producer_name': ('django.db.models.fields.CharField', [], {'default': "'SynopsLive'", 'max_length': '255', 'blank': 'True'}),
            'producer_url': ('django.db.models.fields.CharField', [], {'default': "'http://synopslive.net'", 'max_length': '255', 'blank': 'True'}),
            'show': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['deck.Show']", 'unique': 'True', 'primary_key': 'True'}),
            'synopsis': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'top_image': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'top_link_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_button_label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter_button_message': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter_widget': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'deck.producer': {
            'Meta': {'object_name': 'Producer'},
            'external_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'regroup_shows': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'deck.show': {
            'Meta': {'object_name': 'Show'},
            'archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'average_duration': ('django.db.models.fields.IntegerField', [], {'default': '60', 'blank': 'True'}),
            'carton_background_color': ('django.db.models.fields.CharField', [], {'default': "'transparent'", 'max_length': '20'}),
            'carton_centering_strategy': ('django.db.models.fields.CharField', [], {'default': "'stretched'", 'max_length': '20'}),
            'carton_content': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'carton_image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'carton_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['deck.Category']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'copyright': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'equipe': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'}),
            'external_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'external_url_title': ('django.db.models.fields.CharField', [], {'default': '"Visiter le site d\\xc3\\xa9di\\xc3\\xa9 \\xc3\\xa0 l\'\\xc3\\xa9mission"', 'max_length': '255'}),
            'icon_image': ('django.db.models.fields.files.ImageField', [], {'default': "'http://synopslive.net/static/medias/cartons-ng/shows/unknown.png'", 'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'livepage_bg_image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'podcast_itunes': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'podcast_rss': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'producer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['deck.Producer']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '30'}),
            'twitter_button_label': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'twitter_button_message': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_widget': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'deck.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_realname_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pseudo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'websites': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['deck']