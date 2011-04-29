# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'RiconLiturgico'
        db.delete_table('contenido_riconliturgico')

        # Adding model 'RinconLiturgico'
        db.create_table('contenido_rinconliturgico', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 4, 29, 0, 56, 35, 615671))),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('audio', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=250, db_index=True)),
        ))
        db.send_create_signal('contenido', ['RinconLiturgico'])


    def backwards(self, orm):
        
        # Adding model 'RiconLiturgico'
        db.create_table('contenido_riconliturgico', (
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 4, 29, 0, 19, 41, 98590))),
            ('audio', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=250, db_index=True)),
        ))
        db.send_create_signal('contenido', ['RiconLiturgico'])

        # Deleting model 'RinconLiturgico'
        db.delete_table('contenido_rinconliturgico')


    models = {
        'contenido.adjunto': {
            'Meta': {'object_name': 'Adjunto'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
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
            'Meta': {'ordering': "['-fecha']", 'object_name': 'Noticia'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenido.Categoria']"}),
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 29, 0, 56, 35, 613148)'}),
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
        'contenido.publicacion': {
            'Meta': {'object_name': 'Publicacion'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'categoria': ('django.db.models.fields.IntegerField', [], {}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 29, 0, 56, 35, 616668)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portada': ('cieets.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'contenido.rinconliturgico': {
            'Meta': {'object_name': 'RinconLiturgico'},
            'audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 4, 29, 0, 56, 35, 615671)'}),
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
