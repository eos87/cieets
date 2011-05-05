from django.conf.urls.defaults import *

urlpatterns = patterns('cieets.multimedia.views',
    (r'^$', 'index'),
    (r'^playlist.xml', 'playlist'),
    (r'^videos/$', 'videos'),
    (r'^videos/(?P<id>\d+)/$', 'videos'),
    (r'^audio/$', 'audio'),
    (r'^audio/(?P<id>\d+)/$', 'audio'),
    (r'^fototeca/$', 'fototeca'),
    (r'^fototeca/(?P<id>\d+)/$', 'fototeca'),
)


