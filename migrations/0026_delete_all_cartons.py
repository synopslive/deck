# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):
    def forwards(self, orm):
        orm.Carton.objects.all().delete()

    def backwards(self, orm):
        raise RuntimeError("Cannot reverse this migration.")

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
        u'deck.carton': {
            'Meta': {'object_name': 'Carton'},
            'bg_image': ('django.db.models.fields.files.ImageField', [], {'default': "'http://synopslive.net/static/medias/cartons-ng/fonds/terrasse.jpg'", 'max_length': '100', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['deck.Episode']", 'blank': 'True'}),
            'fb_msg': ('django.db.models.fields.CharField', [], {'default': 'u"S\'inscrire \\xe0 l\'\\xe9v\\xe9nement <strong>Facebook</strong>"', 'max_length': '255', 'blank': 'True'}),
            'fb_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'grand_titre': ('django.db.models.fields.CharField', [], {'max_length': "'255'", 'blank': 'True'}),
            'highlighted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'published_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'standalone': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tagline': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tw_msg': ('django.db.models.fields.CharField', [], {'default': "'Tweeter avec'", 'max_length': '255', 'blank': 'True'}),
            'tw_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
            'carton_content': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'carton_image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'carton_title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': "'10'"}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'show': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['deck.Show']"}),
            'shown': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'termined': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
        u'deck.show': {
            'Meta': {'object_name': 'Show'},
            'average_duration': ('django.db.models.fields.IntegerField', [], {'default': '60', 'blank': 'True'}),
            'carton_content': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'carton_image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'carton_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['deck.Category']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'copyright': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'equipe': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'}),
            'icon_image': ('django.db.models.fields.files.ImageField', [], {'default': "'http://synopslive.net/static/medias/cartons-ng/shows/unknown.png'", 'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'livepage_bg_img': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'podcast_itunes': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'podcast_rss': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '30'}),
            'twitter_button_label': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
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
    symmetrical = True
