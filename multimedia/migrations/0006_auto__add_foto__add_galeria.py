# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Foto'
        db.create_table('multimedia_foto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imagen', self.gf('cieets.thumbs.ImageWithThumbsField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('galeria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['multimedia.Galeria'])),
        ))
        db.send_create_signal('multimedia', ['Foto'])

        # Adding model 'Galeria'
        db.create_table('multimedia_galeria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('portada', self.gf('cieets.thumbs.ImageWithThumbsField')(max_length=100)),
        ))
        db.send_create_signal('multimedia', ['Galeria'])


    def backwards(self, orm):
        
        # Deleting model 'Foto'
        db.delete_table('multimedia_foto')

        # Deleting model 'Galeria'
        db.delete_table('multimedia_galeria')


    models = {
        'multimedia.foto': {
            'Meta': {'object_name': 'Foto'},
            'descripcion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'galeria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimedia.Galeria']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('cieets.thumbs.ImageWithThumbsField', [], {'max_length': '100'})
        },
        'multimedia.fotoportada': {
            'Meta': {'object_name': 'FotoPortada'},
            'archivo': ('cieets.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'multimedia.galeria': {
            'Meta': {'object_name': 'Galeria'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portada': ('cieets.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'multimedia.musica': {
            'Meta': {'object_name': 'Musica'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'artista': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 5, 4, 22, 12, 11, 62675)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'multimedia.programaradial': {
            'Meta': {'object_name': 'ProgramaRadial'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participantes': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'multimedia.video': {
            'Meta': {'object_name': 'Video'},
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['multimedia']
