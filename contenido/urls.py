from django.conf.urls.defaults import *

urlpatterns = patterns('cieets.contenido.views',
    (r'^pagina/(?P<slug>[-\w]+)/$', 'pagina_detail'),
    (r'^noticias/$', 'noticias'),
    (r'^noticias/(?P<slug>[-\w]+)/$', 'noticia_detail'),
    (r'^publicaciones/$', 'publicaciones'),
    (r'^publicaciones/(?P<id>\d+)/$', 'publicacion_detail'),
    (r'^rincon-liturgico/(?P<slug>[-\w]+)/$', 'rincon_detail'),
)


