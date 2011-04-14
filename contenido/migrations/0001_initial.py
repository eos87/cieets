# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Comentario'
        db.create_table('contenido_comentario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')()),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('publicado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('contenido', ['Comentario'])

        # Adding model 'Pagina'
        db.create_table('contenido_pagina', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=250, db_index=True)),
        ))
        db.send_create_signal('contenido', ['Pagina'])

        # Adding model 'Categoria'
        db.create_table('contenido_categoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('contenido', ['Categoria'])

        # Adding model 'Noticia'
        db.create_table('contenido_noticia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 4, 13, 20, 46, 26, 649921))),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenido.Categoria'])),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('imagen', self.gf('cieets.thumbs.ImageWithThumbsField')(max_length=100)),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=250, db_index=True)),
        ))
        db.send_create_signal('contenido', ['Noticia'])

        # Adding model 'Evento'
        db.create_table('contenido_evento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateTimeField')()),
            ('fecha_final', self.gf('django.db.models.fields.DateTimeField')()),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('lugar', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=250, db_index=True)),
        ))
        db.send_create_signal('contenido', ['Evento'])

        # Adding model 'RiconLiturgico'
        db.create_table('contenido_riconliturgico', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 4, 13, 20, 46, 26, 651359))),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('audio', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=250, db_index=True)),
        ))
        db.send_create_signal('contenido', ['RiconLiturgico'])


    def backwards(self, orm):
        
        # Deleting model 'Comentario'
        db.delete_table('contenido_comentario')

        # Deleting model 'Pagina'
        db.delete_table('contenido_pagina')

        # Deleting model 'Categoria'
        db.delete_table('contenido_categoria')

        # Deleting model 'Noticia'
        db.delete_table('contenido_noticia')

        # Deleting model 'Evento'
        db.delete_table('contenido_evento')

        # Deleting model 'RiconLiturgico'
        db.delete_table('contenido_riconliturgico')


    models = {
        'contenido.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'contenido.comentario': {
            'Meta': {'object_name': 'Comentario'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'publicado': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'contenido.evento': {
            'Meta': {'object_name': 'Evento'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'fecha_final': ('django.db.models.fields.DateTimeField', [], {}),
            'fecha_inicio': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '250', 'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'contenido.noticia': {
            'Meta': {'object_name': 'Noticia'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenido.Categoria']"}),
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 13, 20, 46, 26, 649921)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('cieets.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '250', 'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'contenido.pagina': {
            'Meta': {'object_name': 'Pagina'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '250', 'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'contenido.riconliturgico': {
            'Meta': {'object_name': 'RiconLiturgico'},
            'audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 13, 20, 46, 26, 651359)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '250', 'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['contenido']
