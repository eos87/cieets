from django.conf.urls.defaults import patterns, include, url
from settings import DEBUG, PROJECT_DIR

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('cieets.contenido.urls')),
    (r'^', include('cieets.multimedia.urls')),

    # Uncomment the next line to enable the admin:    
    url(r'^admin/', include(admin.site.urls)),
)

if DEBUG:
    urlpatterns += patterns('',
                (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': PROJECT_DIR + '/usermedia'}),
                )
