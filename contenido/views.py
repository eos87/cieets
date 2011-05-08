# -*- encoding: utf-8 -*-
from cieets.treemenus.models import *
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson
from models import *

def pagina_detail(request, slug):
    pagina  = get_object_or_404(Pagina, slug=slug)
    return render_to_response('contenido/pagina_detail.html', RequestContext(request, locals()))

def noticias(request):
    categorias = Categoria.objects.all()
    cat = request.GET.get('cat', '')
    if cat:
        selecta = int(cat)
        try:
            noticias = Noticia.objects.filter(categoria__pk=int(cat))
        except:
            pass
    else:
        noticias = Noticia.objects.all().order_by('-fecha')
    return render_to_response('contenido/noticias.html', RequestContext(request, locals()))

def noticia_detail(request, slug):
    noticia = get_object_or_404(Noticia, slug=slug)
    return render_to_response('contenido/noticia_detail.html', RequestContext(request, locals()))

def publicaciones(request):
    publicaciones = Publicacion.objects.all()
    cat = request.GET.get('cat', '')
    if cat:
        try:
            publicaciones = Publicacion.objects.filter(categoria=int(cat))
        except:
            pass

    return render_to_response('contenido/publicaciones.html', RequestContext(request, locals()))

def publicacion_detail(request, id):
    publicacion = get_object_or_404(Publicacion, id=int(id))
    categoria = ((1, u'Revista'), (2, u'Boletín'), (3, u'Módulo'))[publicacion.categoria-1][1]
    otras_publicaciones = Publicacion.objects.all().exclude(id=publicacion.id).order_by('?')[:3]
    return render_to_response('contenido/publicacion_detail.html', RequestContext(request, locals()))

def rincon_detail(request, slug):
    rincon = get_object_or_404(RinconLiturgico, slug=slug)

    return render_to_response('contenido/rincon_detail.html', RequestContext(request, locals()))

def eventos(request):
    if request.is_ajax():
        start = datetime.datetime.fromtimestamp(float(request.GET['start']))
        end = datetime.datetime.fromtimestamp(float(request.GET['end']))
        fecha1 = datetime.date(start.year, start.month, start.day)
        fecha2 = datetime.date(end.year, end.month, end.day)

        eventos = Evento.objects.filter(fecha_inicio__range=(fecha1, fecha2))
        
        var = []
        for evento in eventos:
            if evento.lugar:
                titulo = evento.titulo + ' en ' + evento.lugar
            else:
                titulo = evento.titulo
            d = {
                'id': str(evento.id),
                'title': titulo,
                'start':str(evento.fecha_inicio),
                'end':str(evento.fecha_final),
                'allDay': False,
                'slug': evento.slug
                }
            var.append(d)
        return HttpResponse(simplejson.dumps(var), mimetype='application/json')
    
    return render_to_response('contenido/event_calendar.html', RequestContext(request, locals()))

def evento_detail(request, slug):
    evento = get_object_or_404(Evento, slug=slug)
    return render_to_response('contenido/evento_detail.html', RequestContext(request, locals()))