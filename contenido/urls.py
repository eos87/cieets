from django.conf.urls.defaults import *

urlpatterns = patterns('cieets.contenido.views',
    (r'^pagina/(?P<slug>[-\w]+)/$', 'pagina_detail'),
    (r'^noticias/$', 'noticias'),
    (r'^noticias/(?P<slug>[-\w]+)/$', 'noticia_detail'),
    (r'^publicaciones/$', 'publicaciones'),
    (r'^publicaciones/(?P<id>\d+)/$', 'publicacion_detail'),
    (r'^rincon-liturgico/$', 'rincon_list'),
    (r'^rincon-liturgico/(?P<slug>[-\w]+)/$', 'rincon_detail'),
    (r'^eventos/$', 'eventos'),
    (r'^eventos/cat/(?P<cat>\d+)/$', 'eventos'),
    (r'^eventos/(?P<slug>[-\w]+)/$', 'evento_detail'),
    (r'^eventos-list/$', 'eventos_list'),
    (r'^busqueda/$', 'busqueda'),
)


