from cieets.contenido.models import Evento
from cieets.contenido.models import Noticia
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *
from forms import *

def index(request):
    fotos = FotoPortada.objects.all()
    noticias = Noticia.objects.all().order_by('-fecha')[:5]
    eventos = Evento.objects.all().order_by('-fecha_inicio')[:3]
    try:
        radio_last = ProgramaRadial.objects.latest('fecha')
    except:
        pass
    return render_to_response('index.html', RequestContext(request, locals()))


def playlist(request):
    canciones = Musica.objects.filter(portada=True).order_by('id')[:15]
    return render(request, 'multimedia/playlist.html', {"canciones": canciones},
                  content_type="application/xhtml+xml")

def videos(request, id=0):
    if id != 0:        
        video = get_object_or_404(Video, pk=id)
        return render_to_response('multimedia/video_detail.html', RequestContext(request, locals()))        
    else:
        videos = Video.objects.all()
    return render_to_response('multimedia/videos.html', RequestContext(request, locals()))

def audio(request, id=0):
    if id != 0:
        audio = get_object_or_404(Musica, pk=id)
        return render_to_response('multimedia/audio_detail.html', RequestContext(request, locals()))
    else:
        audios = Musica.objects.all()
    return render_to_response('multimedia/audio.html', RequestContext(request, locals()))

def fototeca(request, id=0):
    if id != 0:
        album = get_object_or_404(Galeria, pk=id)
        return render_to_response('multimedia/fototeca_detail.html', RequestContext(request, locals()))
    else:
        galerias = Galeria.objects.all()
    return render_to_response('multimedia/fototeca.html', RequestContext(request, locals()))

@login_required
def imagen_tiny(request):    
    if request.method == 'POST':
        form = ImagesForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            if 'file' in request.FILES:
                new = Images()
                new.user = request.user
                new.file = request.FILES['file']
                new.save()
                imagen = new
    else:
        form = ImagesForm()

    if request.is_ajax():
        id = request.POST['id']        
        obj = Images.objects.get(pk=int(id))
        if request.user == obj.user:
            obj.delete()
                
    return render_to_response('multimedia/imagen_tiny.html', RequestContext(request, locals()))