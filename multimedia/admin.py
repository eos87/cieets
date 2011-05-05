from django.contrib import admin
from models import *

admin.site.register(FotoPortada)
admin.site.register(ProgramaRadial)
admin.site.register(Video)
admin.site.register(Musica)

class FotoInline(admin.TabularInline):
    model = Foto
    extra = 3

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha']
    list_filter = ['fecha']

    inlines = [FotoInline, ]

admin.site.register(Galeria, GaleriaAdmin)