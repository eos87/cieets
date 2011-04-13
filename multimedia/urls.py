from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('cieets.multimedia.views',
    (r'^$', 'index'),
    (r'^playlist.xml', 'playlist'),
#    (r'^indicadores/$', 'indicadores'),
#    (r'^familia/jefe/$', 'familia_jefe'),
#    (r'^familia/vivecon/$', 'familia_vivecon'),
)


