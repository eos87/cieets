from django.shortcuts import render_to_response, render
from django.template import RequestContext
from models import FotoPortada, ProgramaRadial, Musica

def index(request):
    fotos = FotoPortada.objects.all()
    try:
        radio_last = ProgramaRadial.objects.latest('fecha')
    except:
        pass
    return render_to_response('index.html', RequestContext(request, locals()))


def playlist(request):
    canciones = Musica.objects.all().order_by('id')[:15]
    return render(request, 'multimedia/playlist.html', {"canciones": canciones},
        content_type="application/xhtml+xml")