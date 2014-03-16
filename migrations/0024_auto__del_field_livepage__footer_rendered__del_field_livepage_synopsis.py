# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'LivePage._footer_rendered'
        db.delete_column(u'deck_livepage', '_footer_rendered')

        # Deleting field 'LivePage.synopsis_markup_type'
        db.delete_column(u'deck_livepage', 'synopsis_markup_type')

        # Deleting field 'LivePage._synopsis_rendered'
        db.delete_column(u'deck_livepage', '_synopsis_rendered')

        # Deleting field 'LivePage.footer_markup_type'
        db.delete_column(u'deck_livepage', 'footer_markup_type')


        # Changing field 'LivePage.footer'
        db.alter_column(u'deck_livepage', 'footer', self.gf('django.db.models.fields.TextField')())

        # Changing field 'LivePage.synopsis'
        db.alter_column(u'deck_livepage', 'synopsis', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'UserProfile._description_rendered'
        db.delete_column(u'deck_userprofile', '_description_rendered')

        # Deleting field 'UserProfile._websites_rendered'
        db.delete_column(u'deck_userprofile', '_websites_rendered')

        # Deleting field 'UserProfile.description_markup_type'
        db.delete_column(u'deck_userprofile', 'description_markup_type')

        # Deleting field 'UserProfile.websites_markup_type'
        db.delete_column(u'deck_userprofile', 'websites_markup_type')


        # Changing field 'UserProfile.description'
        db.alter_column(u'deck_userprofile', 'description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'UserProfile.websites'
        db.alter_column(u'deck_userprofile', 'websites', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'Episode._content_rendered'
        db.delete_column(u'deck_episode', '_content_rendered')

        # Deleting field 'Episode.specific_livepage_url'
        db.delete_column(u'deck_episode', 'specific_livepage_url')

        # Deleting field 'Episode.content_markup_type'
        db.delete_column(u'deck_episode', 'content_markup_type')

        # Adding field 'Episode.end_time'
        db.add_column(u'deck_episode', 'end_time',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Episode.shown'
        db.add_column(u'deck_episode', 'shown',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Episode.carton_title'
        db.add_column(u'deck_episode', 'carton_title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Episode.carton_content'
        db.add_column(u'deck_episode', 'carton_content',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Episode.carton_image'
        db.add_column(u'deck_episode', 'carton_image',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Episode.priority'
        db.add_column(u'deck_episode', 'priority',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


        # Changing field 'Episode.content'
        db.alter_column(u'deck_episode', 'content', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'Show._description_rendered'
        db.delete_column(u'deck_show', '_description_rendered')

        # Deleting field 'Show.description_markup_type'
        db.delete_column(u'deck_show', 'description_markup_type')

        # Deleting field 'Show.livepage_url'
        db.delete_column(u'deck_show', 'livepage_url')

        # Adding field 'Show.average_duration'
        db.add_column(u'deck_show', 'average_duration',
                      self.gf('django.db.models.fields.IntegerField')(default=60, blank=True),
                      keep_default=False)

        # Adding field 'Show.carton_title'
        db.add_column(u'deck_show', 'carton_title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Show.carton_content'
        db.add_column(u'deck_show', 'carton_content',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Show.carton_image'
        db.add_column(u'deck_show', 'carton_image',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Show.livepage_bg_img'
        db.add_column(u'deck_show', 'livepage_bg_img',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Show.twitter_button_label'
        db.add_column(u'deck_show', 'twitter_button_label',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Show.twitter_button_message'
        db.add_column(u'deck_show', 'twitter_button_message',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Show.twitter_widget'
        db.add_column(u'deck_show', 'twitter_widget',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Show.copyright'
        db.add_column(u'deck_show', 'copyright',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


        # Changing field 'Show.description'
        db.alter_column(u'deck_show', 'description', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'Carton.tagline_markup_type'
        db.delete_column(u'deck_carton', 'tagline_markup_type')

        # Deleting field 'Carton._tagline_rendered'
        db.delete_column(u'deck_carton', '_tagline_rendered')


        # Changing field 'Carton.tagline'
        db.alter_column(u'deck_carton', 'tagline', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'LivePage._footer_rendered'
        raise RuntimeError("Cannot reverse this migration. 'LivePage._footer_rendered' and its values cannot be restored.")
        # Adding field 'LivePage.synopsis_markup_type'
        db.add_column(u'deck_livepage', 'synopsis_markup_type',
                      self.gf('django.db.models.fields.CharField')(default='markdown', max_length=30, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'LivePage._synopsis_rendered'
        raise RuntimeError("Cannot reverse this migration. 'LivePage._synopsis_rendered' and its values cannot be restored.")
        # Adding field 'LivePage.footer_markup_type'
        db.add_column(u'deck_livepage', 'footer_markup_type',
                      self.gf('django.db.models.fields.CharField')(default='markdown', max_length=30, blank=True),
                      keep_default=False)


        # Changing field 'LivePage.footer'
        db.alter_column(u'deck_livepage', 'footer', self.gf('markupfield.fields.MarkupField')(rendered_field=True))

        # Changing field 'LivePage.synopsis'
        db.alter_column(u'deck_livepage', 'synopsis', self.gf('markupfield.fields.MarkupField')(rendered_field=True))

        # User chose to not deal with backwards NULL issues for 'UserProfile._description_rendered'
        raise RuntimeError("Cannot reverse this migration. 'UserProfile._description_rendered' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'UserProfile._websites_rendered'
        raise RuntimeError("Cannot reverse this migration. 'UserProfile._websites_rendered' and its values cannot be restored.")
        # Adding field 'UserProfile.description_markup_type'
        db.add_column(u'deck_userprofile', 'description_markup_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.websites_markup_type'
        db.add_column(u'deck_userprofile', 'websites_markup_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)


        # Changing field 'UserProfile.description'
        db.alter_column(u'deck_userprofile', 'description', self.gf('markupfield.fields.MarkupField')(rendered_field=True))

        # Changing field 'UserProfile.websites'
        db.alter_column(u'deck_userprofile', 'websites', self.gf('markupfield.fields.MarkupField')(rendered_field=True))

        # User chose to not deal with backwards NULL issues for 'Episode._content_rendered'
        raise RuntimeError("Cannot reverse this migration. 'Episode._content_rendered' and its values cannot be restored.")
        # Adding field 'Episode.specific_livepage_url'
        db.add_column(u'deck_episode', 'specific_livepage_url',
                      self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Episode.content_markup_type'
        db.add_column(u'deck_episode', 'content_markup_type',
                      self.gf('django.db.models.fields.CharField')(default='markdown', max_length=30),
                      keep_default=False)

        # Deleting field 'Episode.end_time'
        db.delete_column(u'deck_episode', 'end_time')

        # Deleting field 'Episode.shown'
        db.delete_column(u'deck_episode', 'shown')

        # Deleting field 'Episode.carton_title'
        db.delete_column(u'deck_episode', 'carton_title')

        # Deleting field 'Episode.carton_content'
        db.delete_column(u'deck_episode', 'carton_content')

        # Deleting field 'Episode.carton_image'
        db.delete_column(u'deck_episode', 'carton_image')

        # Deleting field 'Episode.priority'
        db.delete_column(u'deck_episode', 'priority')


        # Changing field 'Episode.content'
        db.alter_column(u'deck_episode', 'content', self.gf('markupfield.fields.MarkupField')(rendered_field=True))

        # User chose to not deal with backwards NULL issues for 'Show._description_rendered'
        raise RuntimeError("Cannot reverse this migration. 'Show._description_rendered' and its values cannot be restored.")
        # Adding field 'Show.description_markup_type'
        db.add_column(u'deck_show', 'description_markup_type',
                      self.gf('django.db.models.fields.CharField')(default='markdown', max_length=30, blank=True),
                      keep_default=False)

        # Adding field 'Show.livepage_url'
        db.add_column(u'deck_show', 'livepage_url',
                      self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Show.average_duration'
        db.delete_column(u'deck_show', 'average_duration')

        # Deleting field 'Show.carton_title'
        db.delete_column(u'deck_show', 'carton_title')

        # Deleting field 'Show.carton_content'
        db.delete_column(u'deck_show', 'carton_content')

        # Deleting field 'Show.carton_image'
        db.delete_column(u'deck_show', 'carton_image')

        # Deleting field 'Show.livepage_bg_img'
        db.delete_column(u'deck_show', 'livepage_bg_img')

        # Deleting field 'Show.twitter_button_label'
        db.delete_column(u'deck_show', 'twitter_button_label')

        # Deleting field 'Show.twitter_button_message'
        db.delete_column(u'deck_show', 'twitter_button_message')

        # Deleting field 'Show.twitter_widget'
        db.delete_column(u'deck_show', 'twitter_widget')

        # Deleting field 'Show.copyright'
        db.delete_column(u'deck_show', 'copyright')


        # Changing field 'Show.description'
        db.alter_column(u'deck_show', 'description', self.gf('markupfield.fields.MarkupField')(rendered_field=True))
        # Adding field 'Carton.tagline_markup_type'
        db.add_column(u'deck_carton', 'tagline_markup_type',
                      self.gf('django.db.models.fields.CharField')(default='markdown', max_length=30, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Carton._tagline_rendered'
        raise RuntimeError("Cannot reverse this migration. 'Carton._tagline_rendered' and its values cannot be restored.")

        # Changing field 'Carton.tagline'
        db.alter_column(u'deck_carton', 'tagline', self.gf('markupfield.fields.MarkupField')(rendered_field=True))

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