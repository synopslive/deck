# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'UserProfile'
        db.create_table('deck_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('pseudo', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('websites', self.gf('markupfield.fields.MarkupField')(rendered_field=True, blank=True)),
            ('description', self.gf('markupfield.fields.MarkupField')(rendered_field=True, blank=True)),
            ('websites_markup_type', self.gf('django.db.models.fields.CharField')(default='markdown', max_length=30, blank=True)),
            ('description_markup_type', self.gf('django.db.models.fields.CharField')(default='markdown', max_length=30, blank=True)),
            ('_websites_rendered', self.gf('django.db.models.fields.TextField')()),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('_description_rendered', self.gf('django.db.models.fields.TextField')()),
            ('is_realname_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('deck', ['UserProfile'])

        # Adding model 'Show'
        db.create_table('deck_show', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('short', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=30, db_index=True)),
            ('description', self.gf('markupfield.fields.MarkupField')(rendered_field=True, blank=True)),
            ('description_markup_type', self.gf('django.db.models.fields.CharField')(default=None, max_length=30, blank=True)),
            ('_description_rendered', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('deck', ['Show'])

        # Adding M2M table for field equipe on 'Show'
        db.create_table('deck_show_equipe', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('show', models.ForeignKey(orm['deck.show'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('deck_show_equipe', ['show_id', 'user_id'])

        # Adding model 'Episode'
        db.create_table('deck_episode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('show', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['deck.Show'])),
            ('number', self.gf('django.db.models.fields.CharField')(max_length='10')),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('content', self.gf('markupfield.fields.MarkupField')(rendered_field=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('content_markup_type', self.gf('django.db.models.fields.CharField')(default='markdown', max_length=30)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('_content_rendered', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('deck', ['Episode'])

        # Adding model 'Carton'
        db.create_table('deck_carton', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('episode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['deck.Episode'], blank=True)),
            ('standalone', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fb_msg', self.gf('django.db.models.fields.CharField')(default="S'inscrire \xc3\xa0 l'\xc3\xa9v\xc3\xa9nement <strong>Facebook</strong>", max_length=255)),
            ('fb_url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('tw_msg', self.gf('django.db.models.fields.CharField')(default="S'inscrire \xc3\xa0 l'\xc3\xa9v\xc3\xa9nement <strong>Facebook</strong>", max_length=255)),
            ('tw_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('deck', ['Carton'])


    def backwards(self, orm):
        
        # Deleting model 'UserProfile'
        db.delete_table('deck_userprofile')

        # Deleting model 'Show'
        db.delete_table('deck_show')

        # Removing M2M table for field equipe on 'Show'
        db.delete_table('deck_show_equipe')

        # Deleting model 'Episode'
        db.delete_table('deck_episode')

        # Deleting model 'Carton'
        db.delete_table('deck_carton')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'deck.carton': {
            'Meta': {'object_name': 'Carton'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['deck.Episode']", 'blank': 'True'}),
            'fb_msg': ('django.db.models.fields.CharField', [], {'default': '"S\'inscrire \\xc3\\xa0 l\'\\xc3\\xa9v\\xc3\\xa9nement <strong>Facebook</strong>"', 'max_length': '255'}),
            'fb_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'standalone': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tw_msg': ('django.db.models.fields.CharField', [], {'default': '"S\'inscrire \\xc3\\xa0 l\'\\xc3\\xa9v\\xc3\\xa9nement <strong>Facebook</strong>"', 'max_length': '255'}),
            'tw_url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'deck.episode': {
            'Meta': {'object_name': 'Episode'},
            '_content_rendered': ('django.db.models.fields.TextField', [], {}),
            'content': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'content_markup_type': ('django.db.models.fields.CharField', [], {'default': "'markdown'", 'max_length': '30'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': "'10'"}),
            'show': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['deck.Show']"}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        'deck.show': {
            'Meta': {'object_name': 'Show'},
            '_description_rendered': ('django.db.models.fields.TextField', [], {}),
            'description': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True', 'blank': 'True'}),
            'description_markup_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'blank': 'True'}),
            'equipe': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '30', 'db_index': 'True'})
        },
        'deck.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            '_description_rendered': ('django.db.models.fields.TextField', [], {}),
            '_websites_rendered': ('django.db.models.fields.TextField', [], {}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'description': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True', 'blank': 'True'}),
            'description_markup_type': ('django.db.models.fields.CharField', [], {'default': "'markdown'", 'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_realname_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pseudo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'websites': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True', 'blank': 'True'}),
            'websites_markup_type': ('django.db.models.fields.CharField', [], {'default': "'markdown'", 'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['deck']
