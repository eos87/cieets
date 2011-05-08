from django.contrib import admin
from cieets.contenido.admin import BaseAdmin
from models import *

class MusicaAdmin(BaseAdmin):
    list_display = ['titulo', 'fecha', 'artista', 'portada']
    list_filter = ['artista', 'fecha']
    search_fields = ['artista', 'titulo']

class VideoAdmin(BaseAdmin):    
    search_fields = ['descripcion', 'titulo']

admin.site.register(FotoPortada)
admin.site.register(ProgramaRadial, BaseAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Musica, MusicaAdmin)

class FotoInline(admin.TabularInline):
    model = Foto
    extra = 3

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha']
    list_filter = ['fecha']

    inlines = [FotoInline, ]

admin.site.register(Galeria, GaleriaAdmin)