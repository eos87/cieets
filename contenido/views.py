from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from cieets.treemenus.models import *
from models import Pagina, Categoria, Noticia, Publicacion

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