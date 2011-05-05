# -*- encoding: utf-8 -*-
from django.db import models
from cieets.utils import get_file_path, get_image_path
from cieets.thumbs import ImageWithThumbsField
import datetime

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^cieets\.thumbs\.ImageWithThumbsField"])

class FotoPortada(models.Model):
    nombre = models.CharField(max_length=100)
    archivo = ImageWithThumbsField(upload_to=get_file_path, sizes=((122, 91), ), help_text='Formatos: .jpg .png .gif')    

    fileDir = 'multimedia/portada/'

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        verbose_name = u'Foto de portada'
        verbose_name_plural = u'Fotos de portada'

class ProgramaRadial(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateTimeField();
    archivo = models.FileField(upload_to=get_file_path, help_text='Formato: .mp3')
    descripcion = models.TextField(blank=True, default='')
    participantes = models.CharField(max_length=300, help_text='Nombres separados por coma.', blank=True, default='')

    fileDir = 'multimedia/radio/'

    def __unicode__(self):
        return u'%s' % self.titulo

    class Meta:
        verbose_name = u'Programa radial'
        verbose_name_plural = u'Programas radiales'

class Video(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, default='')
    url = models.CharField(max_length=1000, help_text='http://www.youtube.com/watch?v=p4D9UNXKGV4')

    def __unicode__(self):
        return u'%s' % self.titulo

    def get_absolute_url(self):
        return '/videos/%s' % self.id

    class Meta:
        verbose_name_plural = u'Videos'

class Musica(models.Model):
    portada = models.BooleanField(verbose_name=u'En portada')
    titulo = models.CharField(max_length=100)
    fecha = models.DateTimeField(default=datetime.datetime.now())
    artista = models.CharField(max_length=100)
    archivo = models.FileField(upload_to=get_file_path, help_text='Formato: .mp3')
    descripcion = models.TextField(blank=True, default='')

    fileDir = 'multimedia/musica/'

    def __unicode__(self):
        return u'%s' % self.titulo

    def get_absolute_url(self):
        return '/audio/%s' % self.id

    class Meta:
        verbose_name = u'Música'
        verbose_name_plural = u'Música'

class Galeria(models.Model):
    titulo = models.CharField(max_length=150)
    fecha = models.DateField()
    portada = ImageWithThumbsField(upload_to=get_file_path, sizes=((200, 150), ), help_text='Formatos: .jpg .png .gif')

    fileDir = 'multimedia/galeria/'

    def __unicode__(self):
        return u'%s' % self.titulo

    def get_absolute_url(self):
        return '/fototeca/%s' % self.id

    class Meta:
        verbose_name = u'Galería'
        verbose_name_plural = u'Galerías'

class Foto(models.Model):
    imagen = ImageWithThumbsField(upload_to=get_image_path, sizes=((200, 150), ), help_text='Formatos: .jpg .png .gif')
    descripcion = models.CharField(max_length=200, blank=True, default='')
    galeria = models.ForeignKey(Galeria)

    imgDir = 'multimedia/galeria/'

    def __unicode__(self):
        return u'%s' % self.id

    class Meta:
        verbose_name_plural = u'Fotos'