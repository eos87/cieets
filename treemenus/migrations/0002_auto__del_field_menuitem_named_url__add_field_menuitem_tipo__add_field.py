# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'MenuItem.named_url'
        db.delete_column('treemenus_menuitem', 'named_url')

        # Adding field 'MenuItem.tipo'
        db.add_column('treemenus_menuitem', 'tipo', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)

        # Adding field 'MenuItem.pagina'
        db.add_column('treemenus_menuitem', 'pagina', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contenido.Pagina'], unique=True, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'MenuItem.named_url'
        db.add_column('treemenus_menuitem', 'named_url', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True), keep_default=False)

        # Deleting field 'MenuItem.tipo'
        db.delete_column('treemenus_menuitem', 'tipo')

        # Deleting field 'MenuItem.pagina'
        db.delete_column('treemenus_menuitem', 'pagina_id')


    models = {
        'contenido.pagina': {
            'Meta': {'object_name': 'Pagina'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '250', 'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'treemenus.menu': {
            'Meta': {'object_name': 'Menu'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'levels': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'root_item': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'is_root_item_of'", 'null': 'True', 'to': "orm['treemenus.MenuItem']"})
        },
        'treemenus.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contained_items'", 'null': 'True', 'to': "orm['treemenus.Menu']"}),
            'pagina': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contenido.Pagina']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['treemenus.MenuItem']", 'null': 'True', 'blank': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['treemenus']
