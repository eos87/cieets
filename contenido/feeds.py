# -*- encoding: utf-8 -*-

from django.contrib.syndication.views import Feed
from models import Noticia

class NoticiasFeed(Feed):
    title = "Noticias Cieets"
    link = "/noticias/"
    description = "Actualizaciones de noticias de cieets.org.ni"

    def items(self):
        return Noticia.objects.order_by('-fecha')[:10]

    def item_title(self, item):
        return item.titulo

    def item_description(self, item):
        return item.contenido
