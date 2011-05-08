from django.contrib import admin
from django.contrib.contenttypes import generic
from models import *

class BaseAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    
    class Media:
        js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/tconfig.js')

class AdjuntoInline(generic.GenericTabularInline):
    model = Adjunto
    extra = 1

class NoticiaAdmin(BaseAdmin):
    search_fields = ['titulo', 'contenido', 'autor']
    list_display = ['titulo', 'fecha', 'autor']
    list_filter = ['categoria__nombre', 'autor']
    list_per_page = 25
    save_on_top = True
    actions_on_top = True

    inlines = [AdjuntoInline, ]

class EventoAdmin(BaseAdmin):
    search_fields = ['titulo', 'contenido']
    list_display = ['titulo', 'fecha_inicio', 'fecha_final', 'lugar']
    list_filter = ['fecha_inicio', 'fecha_final']
    list_per_page = 25
    save_on_top = True
    actions_on_top = True

class PublicacionAdmin(BaseAdmin):
    list_display = ['titulo', 'fecha', 'categoria']
    list_filter = ['categoria', 'fecha']
    list_per_page = 25
    save_on_top = True
    actions_on_top = True

class RinconAdmin(BaseAdmin):
    list_display = ['titulo', 'fecha', 'autor']
    list_filter = ['autor', 'fecha']
    list_per_page = 25
    save_on_top = True
    actions_on_top = True

    inlines = [AdjuntoInline, ]

admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Pagina, BaseAdmin)
admin.site.register(Categoria)
admin.site.register(RinconLiturgico, RinconAdmin)
admin.site.register(Publicacion, PublicacionAdmin)


