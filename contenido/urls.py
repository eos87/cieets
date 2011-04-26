from django.conf.urls.defaults import *

urlpatterns = patterns('cieets.contenido.views',
    (r'^pagina/(?P<slug>[-\w]+)/$', 'pagina_detail'),
    (r'^noticias/$', 'noticias'),
    (r'^noticias/(?P<slug>[-\w]+)/$', 'noticia_detail'),
#    (r'^familia/vivecon/$', 'familia_vivecon'),
)


