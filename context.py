from cieets.contenido.models import *

def variables(request):
    dicc = {}
    revista = None
    boletin = None
    modulo = None
    rincon = None
    try:
        revista = Publicacion.objects.filter(categoria=1).latest('fecha')
    except:
        pass
    try:
        boletin = Publicacion.objects.filter(categoria=2).latest('fecha')
    except:
        pass
    try:
        modulo = Publicacion.objects.filter(categoria=3).latest('fecha')
    except:
        pass
    try:
        rincon = RinconLiturgico.objects.latest('fecha')
    except:
        pass
    
    dicc = {
        'revista': revista,
        'boletin': boletin,
        'modulo': modulo,
        'rincon': rincon,
    }
    return dicc

