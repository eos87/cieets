# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.template.defaultfilters import slugify
from cieets.utils import get_file_path
from cieets.thumbs import ImageWithThumbsField
import datetime

class Adjunto(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    nombre = models.CharField(max_length=100)
    archivo = models.FileField(upload_to=get_file_path)

    fileDir = 'contenido/attachments/'

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        verbose_name_plural = u'Adjuntos'

class Comentario(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    contenido = models.TextField()
    publicado = models.BooleanField()
    
    def __unicode__(self):
        return self.id
    
    class Meta:
        verbose_name_plural = u'Comentarios'

class Pagina(models.Model):
    """Modelo que contiene la mayoria del texto casi estatico mayormente linkeado con el menu"""
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    slug = models.SlugField(max_length=250, editable=False)

    def __unicode__(self):
        return u'%s' % self.titulo

    def get_absolute_url(self):
        return u'/pagina/%s' % self.slug

    def save(self):
        if not self.id:
            n = Pagina.objects.all().count()
            self.slug = '%s-%s' % (str(n + 1), slugify(self.titulo))
        else:
            pass
        super(Pagina, self).save()

    class Meta:
        verbose_name = u'Página'
        verbose_name_plural = u'Páginas'

class Categoria(models.Model):
    nombre = models.CharField(max_length=150)

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        verbose_name_plural = u'Categorias'

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=datetime.datetime.now())
    categoria = models.ForeignKey(Categoria)
    autor = models.CharField(max_length=200)
    imagen = ImageWithThumbsField(upload_to=get_file_path, sizes=((78, 81), (180, 86), (225, 168), (231, 174)), help_text='Formatos: .jpg .png .gif')
    contenido = models.TextField()
    slug = models.SlugField(max_length=250, editable=False)
    comentario = generic.GenericRelation(Comentario)
    adjunto = generic.GenericRelation(Adjunto)

    fileDir = 'contenido/noticia/'

    def __unicode__(self):
        return u'%s' % self.titulo

    def get_absolute_url(self):
        return u'/noticias/%s' % self.slug

    def save(self):
        if not self.id:
            n = Noticia.objects.all().count()
            self.slug = '%s-%s' % (str(n + 1), slugify(self.titulo))
        else:
            pass
        super(Noticia, self).save()

    class Meta:
        ordering = ['-fecha']
        verbose_name = u'Noticia'
        verbose_name_plural = u'Noticias'

class CategoriaEvento(models.Model):
    nombre = models.CharField(max_length=150)

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        verbose_name = u'Categoria de evento'
        verbose_name_plural = u'Categorias de los eventos'

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    categoria = models.ForeignKey(CategoriaEvento)
    contenido = models.TextField()
    lugar = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, editable=False)

    def __unicode__(self):
        return u'%s' % self.titulo

    def get_absolute_url(self):
        return u'/eventos/%s' % self.slug

    def save(self):
        if not self.id:
            n = Evento.objects.all().count()
            self.slug = '%s-%s' % (str(n + 1), slugify(self.titulo))
        else:
            pass
        super(Evento, self).save()

    class Meta:
        verbose_name_plural = u'Eventos'

class CategoriaRincon(models.Model):
    nombre = models.CharField(max_length=150)

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        verbose_name = u'Categoria Rincón Litúrgico'
        verbose_name_plural = u'Categorias Rincón Litúrgico'

class RinconLiturgico(models.Model):    
    titulo = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=datetime.datetime.now())    
    autor = models.CharField(max_length=200)
    categoria = models.ForeignKey(CategoriaRincon)
    contenido = models.TextField()
    audio = models.FileField(upload_to=get_file_path, help_text=u'Formato: .mp3', blank=True, null=True)
    slug = models.SlugField(max_length=250, editable=False)
    adjunto = generic.GenericRelation(Adjunto)

    fileDir = 'contenido/rincon/'

    def __unicode__(self):
        return u'%s' % self.titulo

    def get_absolute_url(self):
        return u'/rincon-liturgico/%s' % self.slug

    def save(self):
        if not self.id:
            n = RinconLiturgico.objects.all().count()
            self.slug = '%s-%s' % (str(n + 1), slugify(self.titulo))
        else:
            pass
        super(RinconLiturgico, self).save()

    class Meta:
        verbose_name_plural = u'Rincones Litúrgicos'

class Publicacion(models.Model):
    titulo = models.CharField(max_length=150)
    categoria = models.IntegerField(choices=((1, u'Revista'), (2, u'Boletín'), (3, u'Módulo')))
    portada = ImageWithThumbsField(upload_to=get_file_path, sizes=((67, 90), (176, 238)), help_text='Formatos: .jpg .png .gif')
    fecha = models.DateTimeField(default=datetime.datetime.now())
    descripcion = models.TextField()
    archivo = models.FileField(upload_to=get_file_path, blank=True, null=True)

    fileDir = 'contenido/publicaciones/'

    def __unicode__(self):
        return u'%s' % self.titulo

    def get_absolute_url(self):
        return u'/publicaciones/%s' % self.id

    class Meta:
        verbose_name = u'Publicación'
        verbose_name_plural = u'Publicaciones'
