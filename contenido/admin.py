from django.contrib import admin
from django.contrib.contenttypes import generic
from models import *

class AdjuntoInline(generic.GenericTabularInline):
    model = Adjunto
    extra = 1

class NoticiaAdmin(admin.ModelAdmin):
    search_fields = ['titulo', 'contenido', 'autor']
    list_display = ['titulo', 'fecha', 'autor']
    list_filter = ['categoria__nombre', 'autor']
    list_per_page = 25
    save_on_top = True
    actions_on_top = True

    inlines = [AdjuntoInline, ]

class EventoAdmin(admin.ModelAdmin):
    search_fields = ['titulo', 'contenido']
    list_display = ['titulo', 'fecha_inicio', 'fecha_final', 'lugar']
    list_filter = ['fecha_inicio', 'fecha_final']
    list_per_page = 25
    save_on_top = True
    actions_on_top = True

class PublicacionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha', 'categoria']
    list_filter = ['categoria', 'fecha']
    list_per_page = 25
    save_on_top = True
    actions_on_top = True

admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Pagina)
admin.site.register(Categoria)
admin.site.register(RinconLiturgico)
admin.site.register(Publicacion, PublicacionAdmin)


