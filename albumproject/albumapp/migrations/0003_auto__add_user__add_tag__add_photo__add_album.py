# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'albumapp_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('pwdhash', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'albumapp', ['User'])

        # Adding model 'Tag'
        db.create_table(u'albumapp_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'albumapp', ['Tag'])

        # Adding model 'Photo'
        db.create_table(u'albumapp_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['albumapp.User'])),
        ))
        db.send_create_signal(u'albumapp', ['Photo'])

        # Adding M2M table for field tags on 'Photo'
        m2m_table_name = db.shorten_name(u'albumapp_photo_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photo', models.ForeignKey(orm[u'albumapp.photo'], null=False)),
            ('tag', models.ForeignKey(orm[u'albumapp.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['photo_id', 'tag_id'])

        # Adding model 'Album'
        db.create_table(u'albumapp_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['albumapp.User'])),
        ))
        db.send_create_signal(u'albumapp', ['Album'])

        # Adding M2M table for field photos on 'Album'
        m2m_table_name = db.shorten_name(u'albumapp_album_photos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('album', models.ForeignKey(orm[u'albumapp.album'], null=False)),
            ('photo', models.ForeignKey(orm[u'albumapp.photo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['album_id', 'photo_id'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'albumapp_user')

        # Deleting model 'Tag'
        db.delete_table(u'albumapp_tag')

        # Deleting model 'Photo'
        db.delete_table(u'albumapp_photo')

        # Removing M2M table for field tags on 'Photo'
        db.delete_table(db.shorten_name(u'albumapp_photo_tags'))

        # Deleting model 'Album'
        db.delete_table(u'albumapp_album')

        # Removing M2M table for field photos on 'Album'
        db.delete_table(db.shorten_name(u'albumapp_album_photos'))


    models = {
        u'albumapp.album': {
            'Meta': {'object_name': 'Album'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['albumapp.User']"}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['albumapp.Photo']", 'symmetrical': 'False'})
        },
        u'albumapp.photo': {
            'Meta': {'object_name': 'Photo'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['albumapp.User']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['albumapp.Tag']", 'symmetrical': 'False'})
        },
        u'albumapp.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'albumapp.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'pwdhash': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['albumapp']